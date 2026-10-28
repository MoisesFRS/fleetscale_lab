import uuid
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import Base, engine, get_session
from app.models.entities import Position, Vehicle
from app.schemas.payloads import PositionCreate, PositionRead, VehicleCreate, VehicleRead


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Apenas laboratorio. Na evolucao, usar Alembic para controlar migracoes.
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(title="FleetScale Lab", version="0.1.0", lifespan=lifespan)


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/readyz")
async def readyz(session: AsyncSession = Depends(get_session)):
    await session.execute(text("SELECT 1"))
    return {"status": "ready"}


@app.post("/api/v1/vehicles", response_model=VehicleRead, status_code=status.HTTP_201_CREATED)
async def register_vehicle(body: VehicleCreate, session: AsyncSession = Depends(get_session)):
    vehicle = Vehicle(external_id=body.external_id)
    session.add(vehicle)
    try:
        await session.commit()
        await session.refresh(vehicle)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=409, detail="external_id ja cadastrado") from None
    return vehicle


@app.post("/api/v1/positions", response_model=PositionRead, status_code=status.HTTP_201_CREATED)
async def create_position(body: PositionCreate, session: AsyncSession = Depends(get_session)):
    if await session.get(Vehicle, body.vehicle_id) is None:
        raise HTTPException(status_code=404, detail="veiculo nao encontrado")
    position = Position(**body.model_dump())
    session.add(position)
    await session.commit()
    await session.refresh(position)
    return position


@app.get("/api/v1/vehicles/{vehicle_id}/location/latest", response_model=PositionRead)
async def latest_position(vehicle_id: uuid.UUID, session: AsyncSession = Depends(get_session)):
    statement = (
        select(Position)
        .where(Position.vehicle_id == vehicle_id)
        .order_by(Position.recorded_at.desc(), Position.id.desc())
        .limit(1)
    )
    position = (await session.execute(statement)).scalar_one_or_none()
    if position is None:
        raise HTTPException(status_code=404, detail="posicao nao encontrada")
    return position

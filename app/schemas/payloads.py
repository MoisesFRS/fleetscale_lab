import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class VehicleCreate(BaseModel):
    external_id: str = Field(min_length=1, max_length=80)


class VehicleRead(VehicleCreate):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    created_at: datetime


class PositionCreate(BaseModel):
    vehicle_id: uuid.UUID
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    speed_kmh: float | None = Field(default=None, ge=0, le=300)
    recorded_at: datetime

    @field_validator("recorded_at")
    @classmethod
    def needs_timezone(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("recorded_at must include an explicit timezone")
        return value


class PositionRead(PositionCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    received_at: datetime

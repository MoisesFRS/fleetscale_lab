from datetime import datetime, timezone
import uuid

import pytest
from pydantic import ValidationError

from app.schemas.payloads import PositionCreate, VehicleCreate


def test_valid_position():
    position = PositionCreate(
        vehicle_id=uuid.uuid4(),
        latitude=-23.0021,
        longitude=-46.8465,
        recorded_at=datetime.now(timezone.utc),
    )
    assert position.speed_kmh is None


@pytest.mark.parametrize("latitude", [-90.01, 90.01])
def test_invalid_latitude(latitude):
    with pytest.raises(ValidationError):
        PositionCreate(
            vehicle_id=uuid.uuid4(),
            latitude=latitude,
            longitude=-46.0,
            recorded_at=datetime.now(timezone.utc),
        )


def test_reject_naive_time():
    with pytest.raises(ValidationError):
        PositionCreate(
            vehicle_id=uuid.uuid4(),
            latitude=0,
            longitude=0,
            recorded_at=datetime(2026, 10, 28, 12),
        )


def test_empty_external_id_rejected():
    with pytest.raises(ValidationError):
        VehicleCreate(external_id="")

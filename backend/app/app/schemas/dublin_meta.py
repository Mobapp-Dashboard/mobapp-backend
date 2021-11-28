from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class DublinMetaBase(BaseModel):
    trajectory_id: Optional[int]
    # line_id: Optional[int]
    journey_id: Optional[str]
    time_frame: Optional[datetime]
    vehicle_journey_id: Optional[int]
    operator: Optional[str]
    vehicle_id: Optional[int]
    # trajectory_size: Optional[int]
    first_lat: Optional[float]
    last_lat: Optional[float]
    first_lng: Optional[float]
    last_lng: Optional[float]
    first_instant: Optional[datetime]
    last_instant: Optional[datetime]


class DublinField(BaseModel):
    class Config:
        orm_mode = True


class DublinLines(DublinField):
    journey_id: Optional[str]


class DublinTrajs(DublinField):
    trajectory_id: Optional[int]


class DublinJourneys(DublinField):
    journey_id: Optional[str]


# Properties to receive on item creation
class DublinMetaCreate(DublinMetaBase):
    pass


# Properties to receive on item update
class DublinMetaUpdate(DublinMetaBase):
    pass


# Properties shared by models stored in DB
class DublinMetaInDBBase(DublinMetaBase):
    class Config:
        orm_mode = True


# Properties to return to client
class DublinMeta(DublinMetaInDBBase):
    pass


# Properties properties stored in DB
class DublinMetaInDB(DublinMetaInDBBase):
    pass

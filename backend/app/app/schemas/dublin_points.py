#!/usr/bin/env ipython

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Shared properties
class DublinPointsBase(BaseModel):
    id : Optional[int]
    trajectory_id : Optional[int]
    instant : Optional[datetime]
    lat : Optional[float]
    lng : Optional[float]
    lat_mercator : Optional[float]
    lng_mercator : Optional[float]
    speed : Optional[float]
    acceleration : Optional[float]
    position : Optional[float]
    delta_dist : Optional[float]
    delta_time : Optional[float]
    bearing : Optional[float]
    year : Optional[int]
    month : Optional[int]
    day : Optional[int]
    hour : Optional[int]
    minute : Optional[int]
    stop_labels : Optional[bool]


# Properties to receive on item creation
class DublinPointsCreate(DublinPointsBase):
    pass

# Properties to receive on item update
class DublinPointsUpdate(DublinPointsBase):
    pass


# Properties shared by models stored in DB
class DublinPointsInDBBase(DublinPointsBase):
    class Config:
        orm_mode = True


# Properties to return to client
class DublinPoints(DublinPointsInDBBase):
    pass

# Properties properties stored in DB
class DublinPointsInDB(DublinPointsInDBBase):
    pass

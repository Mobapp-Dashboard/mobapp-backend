#!/usr/bin/env ipython

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class DublinModelPointsBase(BaseModel):
    index: Optional[int]
    trajectory_id: Optional[int]
    rota: Optional[int]
    lat: Optional[float]
    lng: Optional[float]


# Properties to receive on item creation
class DublinModelPointsCreate(DublinModelPointsBase):
    pass


# Properties to receive on item update
class DublinModelPointsUpdate(DublinModelPointsBase):
    pass


# Properties shared by models stored in DB
class DublinModelPointsInDBBase(DublinModelPointsBase):
    class Config:
        orm_mode = True


# Properties to return to client
class DublinModelPoints(DublinModelPointsInDBBase):
    pass


# Properties properties stored in DB
class DublinModelPointsInDB(DublinModelPointsInDBBase):
    pass

#!/usr/bin/env ipython

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class DublinModelBase(BaseModel):
    index: Optional[int]
    trajectory_id: Optional[int]
    predicted: Optional[int]
    input_token: Optional[int]
    routes: Optional[int]
    lat: Optional[float]
    lng: Optional[float]


# Properties to receive on item creation
class DublinModelCreate(DublinModelBase):
    pass


# Properties to receive on item update
class DublinModelUpdate(DublinModelBase):
    pass


# Properties shared by models stored in DB
class DublinModelInDBBase(DublinModelBase):
    class Config:
        orm_mode = True


# Properties to return to client
class DublinModel(DublinModelInDBBase):
    pass


# Properties properties stored in DB
class DublinModelInDB(DublinModelInDBBase):
    pass

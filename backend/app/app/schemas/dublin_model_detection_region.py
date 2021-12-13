#!/usr/bin/env ipython

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class DublinModelDetectionRegionBase(BaseModel):
    index: Optional[int]
    model: Optional[str]
    route: Optional[int]
    trajectory_id: Optional[int]
    anom_predictions: Optional[str]
    anom_true: Optional[str]


# Properties to receive on item creation
class DublinModelDetectionRegionCreate(DublinModelDetectionRegionBase):
    pass


# Properties to receive on item update
class DublinModelDetectionRegionUpdate(DublinModelDetectionRegionBase):
    pass


# Properties shared by models stored in DB
class DublinModelDetectionRegionInDBBase(DublinModelDetectionRegionBase):
    class Config:
        orm_mode = True


# Properties to return to client
class DublinModelDetectionRegion(DublinModelDetectionRegionInDBBase):
    pass


# Properties properties stored in DB
class DublinModelDetectionRegionInDB(DublinModelDetectionRegionInDBBase):
    pass

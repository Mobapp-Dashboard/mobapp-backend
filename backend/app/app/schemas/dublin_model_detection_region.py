#!/usr/bin/env ipython

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class DublinPredictionRegionBase(BaseModel):
    index: Optional[int]
    filename: Optional[str]
    rota: Optional[int]
    trajectory_id: Optional[int]
    anon_predictions: Optional[str]
    true_anon: Optional[str]


# Properties to receive on item creation
class DublinPredictionRegionCreate(DublinPredictionRegionBase):
    pass


# Properties to receive on item update
class DublinPredictionRegionUpdate(DublinPredictionRegionBase):
    pass


# Properties shared by models stored in DB
class DublinPredictionRegionInDBBase(DublinPredictionRegionBase):
    class Config:
        orm_mode = True


# Properties to return to client
class DublinPredictionRegion(DublinPredictionRegionInDBBase):
    pass


# Properties properties stored in DB
class DublinPredictionRegionInDB(DublinPredictionRegionInDBBase):
    pass

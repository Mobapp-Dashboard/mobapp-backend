#!/usr/bin/env ipython
from typing import Optional

from pydantic import BaseModel


# Shared properties
class DublinModelScoresBase(BaseModel):
    route: Optional[int]
    trajectory_id: Optional[int]
    model: Optional[str]
    scores: Optional[float]


# Properties to receive on item creation
class DublinModelScoresCreate(DublinModelScoresBase):
    pass


# Properties to receive on item update
class DublinModelScoresUpdate(DublinModelScoresBase):
    pass


# Properties shared by models stored in DB
class DublinModelScoresInDBBase(DublinModelScoresBase):
    class Config:
        orm_mode = True


# Properties to return to client
class DublinModelScores(DublinModelScoresInDBBase):
    pass


# Properties properties stored in DB
class DublinModelScoresInDB(DublinModelScoresInDBBase):
    pass

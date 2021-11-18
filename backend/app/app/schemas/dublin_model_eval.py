#!/usr/bin/env ipython

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class DublinModelEvalBase(BaseModel):
    index: Optional[int]
    model: Optional[str]
    route: Optional[int]
    precision: Optional[float]
    recall: Optional[float]
    threshold: Optional[float]


# Properties to receive on item creation
class DublinModelEvalCreate(DublinModelEvalBase):
    pass


# Properties to receive on item update
class DublinModelEvalUpdate(DublinModelEvalBase):
    pass


# Properties shared by models stored in DB
class DublinModelEvalInDBBase(DublinModelEvalBase):
    class Config:
        orm_mode = True


# Properties to return to client
class DublinModelEval(DublinModelEvalInDBBase):
    pass


# Properties properties stored in DB
class DublinModelEvalInDB(DublinModelEvalInDBBase):
    pass

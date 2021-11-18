#!/usr/bin/env ipython

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class DublinEvalModelsBase(BaseModel):
    index: Optional[int]
    filename: Optional[str]
    rota: Optional[int]
    auc: Optional[float]
    max_f1: Optional[float]
    f1_thr: Optional[float]
    precision: Optional[float]
    recall: Optional[float]
    threshold: Optional[float]


# Properties to receive on item creation
class DublinEvalModelsCreate(DublinEvalModelsBase):
    pass


# Properties to receive on item update
class DublinEvalModelsUpdate(DublinEvalModelsBase):
    pass


# Properties shared by models stored in DB
class DublinEvalModelsInDBBase(DublinEvalModelsBase):
    class Config:
        orm_mode = True


# Properties to return to client
class DublinEvalModels(DublinEvalModelsInDBBase):
    pass


# Properties properties stored in DB
class DublinEvalModelsInDB(DublinEvalModelsInDBBase):
    pass

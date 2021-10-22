#!/usr/bin/env ipython
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

from app.crud.base import CRUDBase
from app.models.dublin_eval_models import DublinEvalModels
from app.schemas.dublin_eval_models import (
    DublinEvalModelsCreate,
    DublinEvalModelsUpdate,
)


class CRUDDublinEvalModels(
    CRUDBase[DublinEvalModels, DublinEvalModelsCreate, DublinEvalModelsUpdate]
):
    def get_by_method_rota(
        self, db: Session, *, method: str, rota: int
    ) -> List[DublinEvalModels]:
        query = (
            db.query(DublinEvalModels)
            .filter(DublinEvalModels.filename == method)
            .filter(DublinEvalModels.rota == rota)
        )
        return query.all()


dublin_eval_models = CRUDDublinEvalModels(DublinEvalModels)

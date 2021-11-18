#!/usr/bin/env ipython
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

from app.crud.base import CRUDBase
from app.models.dublin_model_eval import DublinModelEval
from app.schemas.dublin_model_eval import DublinModelEvalCreate, DublinModelEvalUpdate


class CRUDDublinModelEval(
    CRUDBase[DublinModelEval, DublinModelEvalCreate, DublinModelEvalUpdate]
):
    def get_by_method_rota(
        self, db: Session, *, method: str, rota: int
    ) -> List[DublinModelEval]:
        query = (
            db.query(DublinModelEval)
            .filter(DublinModelEval.filename == method)
            .filter(DublinModelEval.rota == rota)
        )
        return query.all()


dublin_model_eval = CRUDDublinModelEval(DublinModelEval)

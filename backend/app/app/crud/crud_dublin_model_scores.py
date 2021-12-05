#!/usr/bin/env ipython
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

from app.crud.base import CRUDBase
from app.models.dublin_model_scores import DublinModelScores
from app.schemas.dublin_model_scores import (
    DublinModelScoresCreate,
    DublinModelScoresUpdate,
)


class CRUDDublinModelScores(
    CRUDBase[DublinModelScores, DublinModelScoresCreate, DublinModelScoresUpdate]
):
    def get_score_by_route(self, db: Session, *, route: int) -> List[DublinModelScores]:
        query = db.query(DublinModelScores).filter(DublinModelScores.route == route)
        return query.all()


dublin_model_scores = CRUDDublinModelScores(DublinModelScores)

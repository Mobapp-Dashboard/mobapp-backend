#!/usr/bin/env ipython
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

from app.crud.base import CRUDBase
from app.models.dublin_prediction_region import DublinPredictionRegion
from app.schemas.dublin_prediction_region import (
    DublinPredictionRegionCreate,
    DublinPredictionRegionUpdate,
)


class CRUDDublinPredictionRegion(
    CRUDBase[
        DublinPredictionRegion,
        DublinPredictionRegionCreate,
        DublinPredictionRegionUpdate,
    ]
):
    def get_by_method_rota(
        self, db: Session, *, method: str, rota: int
    ) -> List[DublinPredictionRegion]:
        query = (
            db.query(DublinPredictionRegion)
            .filter(DublinPredictionRegion.filename == method)
            .filter(DublinPredictionRegion.rota == rota)
        )
        return query.all()


dublin_prediction_region = CRUDDublinPredictionRegion(DublinPredictionRegion)

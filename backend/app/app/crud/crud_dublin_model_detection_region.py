#!/usr/bin/env ipython
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

from app.crud.base import CRUDBase
from app.models.dublin_model_detection_region import DublinModelDetectionRegion
from app.schemas.dublin_model_detection_region import (
    DublinModelDetectionRegionCreate,
    DublinModelDetectionRegionUpdate,
)


class CRUDDublinModelDetectionRegion(
    CRUDBase[
        DublinModelDetectionRegion,
        DublinModelDetectionRegionCreate,
        DublinModelDetectionRegionUpdate,
    ]
):
    def get_by_method_route(
        self, db: Session, *, method: str, route: int
    ) -> List[DublinModelDetectionRegion]:
        query = (
            db.query(DublinModelDetectionRegion)
            .filter(DublinModelDetectionRegion.model == method)
            .filter(DublinModelDetectionRegion.route == route)
        )
        return query.all()


dublin_model_detection_region = CRUDDublinModelDetectionRegion(
    DublinModelDetectionRegion
)

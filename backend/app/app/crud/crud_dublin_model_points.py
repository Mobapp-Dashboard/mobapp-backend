#!/usr/bin/env ipython

from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.dublin_model_points import DublinModelPoints
from app.schemas.dublin_model_points import (
    DublinModelPointsCreate,
    DublinModelPointsUpdate,
)


class CRUDDublinModelPoints(
    CRUDBase[DublinModelPoints, DublinModelPointsCreate, DublinModelPointsUpdate]
):
    def get_points_by_rota_traj(
        self, db: Session, *, trajectory_id: int = None, rota: int = None
    ) -> List[DublinModelPoints]:
        query = db.query(self.model)
        if trajectory_id is not None:
            query = query.filter(DublinModelPoints.trajectory_id == trajectory_id)
        query = query.filter(DublinModelPoints.rota == rota)
        return query.all()


dublin_model_points = CRUDDublinModelPoints(DublinModelPoints)

#!/usr/bin/env ipython

from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.dublin_points import DublinPoints
from app.schemas.dublin_points import DublinPointsCreate, DublinPointsUpdate


class CRUDDublinPoints(CRUDBase[DublinPoints, DublinPointsCreate, DublinPointsUpdate]):
    def get_by_trajectory(
        self, db: Session, *, traj_id: int, skip: int = 0, limit: int = 100
    ) -> List[DublinPoints]:
        return (
            db.query(self.model)
            .filter(DublinPoints.trajectory_id == traj_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

dublin_points = CRUDDublinPoints(DublinPoints)

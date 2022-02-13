#!/usr/bin/env ipython

from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from app.crud.base import CRUDBase
from app.models.dublin_meta import DublinMeta
from app.models.dublin_points import DublinPoints
from app.schemas.dublin_points import DublinPointsCreate, DublinPointsUpdate


class CRUDDublinPoints(CRUDBase[DublinPoints, DublinPointsCreate, DublinPointsUpdate]):
    def get_by_trajectory(self, db: Session, *, traj_id: int) -> List[DublinPoints]:
        print(traj_id)
        return db.query(self.model).filter(DublinPoints.trajectory_id == traj_id).all()

    def get_random_traj(self, db: Session) -> List[DublinPoints]:
        return db.query(DublinPoints).order_by(func.random()).limit(10).all()

    def get_traj_by_multiparam(
        self, db: Session, *, skip: int = 0, limit: int = 100, **kwargs
    ) -> List[DublinPoints]:

        query = db.query(self.model)

        if "journey_id" in kwargs.keys():
            journey_subquery = (
                db.query(DublinMeta.trajectory_id)
                .distinct()
                .filter(DublinMeta.journey_id == kwargs["journey_id"])
                #                .limit(100)
                .subquery()
            )
            query = query.filter(DublinPoints.trajectory_id.in_(journey_subquery))
            kwargs.pop("journey_id")

        if "turn" in kwargs.keys():
            turno_subquery = (
                db.query(DublinPoints.trajectory_id)
                .distinct()
                .filter(DublinPoints.turn == kwargs["turn"])
                # .limit(100)
                .subquery()
            )
            query = query.filter(DublinPoints.trajectory_id.in_(turno_subquery))
            kwargs.pop("turn")

        date_subquery = (
            db.query(DublinMeta.trajectory_id)
            .distinct()
            .filter(DublinMeta.time_frame >= kwargs["start_date"])
            .filter(DublinMeta.time_frame <= kwargs["end_date"])
            .subquery()
        )
        query = query.filter(DublinPoints.trajectory_id.in_(date_subquery))
        # return query.order_by(func.random()).limit(1000).all()
        return query.limit(100).all()


dublin_points = CRUDDublinPoints(DublinPoints)

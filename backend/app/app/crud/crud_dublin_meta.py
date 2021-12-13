from datetime import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

from app.crud.base import CRUDBase
from app.models.dublin_meta import DublinMeta
from app.schemas.dublin_meta import DublinMetaCreate, DublinMetaUpdate


class CRUDDublinMeta(CRUDBase[DublinMeta, DublinMetaCreate, DublinMetaUpdate]):
    #     def get_by_line_journey(
    #         self,
    #         db: Session,
    #         *,
    #         line_id: int,
    #         journey_id: str,
    #         skip: int = 0,
    #         limit: int = 100,
    #     ) -> List[DublinMeta]:
    #         return (
    #             db.query(self.model)
    #             .filter(
    #                 (DublinMeta.line_id == line_id) & (DublinMeta.journey_id == journey_id)
    #             )
    #             .offset(skip)
    #             .limit(limit)
    #             .all()
    #         )
    #
    #     def get_by_line(
    #         self, db: Session, *, line_id: int, skip: int = 0, limit: int = 100
    #     ) -> List[DublinMeta]:
    #         return (
    #             db.query(self.model)
    #             .filter(DublinMeta.line_id == line_id)
    #             .offset(skip)
    #             .limit(limit)
    #             .all()
    #         )
    #
    def get_by_journey(
        self,
        db: Session,
        *,
        journey_id: str,
        start_date: datetime,
        end_date: datetime,
        skip: int = 0,
        limit: int = 100,
    ) -> List[DublinMeta]:
        return (
            db.query(self.model.trajectory_id)
            .distinct()
            .filter(DublinMeta.journey_id == journey_id)
            .filter(DublinMeta.time_frame <= start_date)
            .filter(DublinMeta.time_frame <= end_date)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_journey_by_date(
        self, db: Session, *, start_date: datetime, end_date: datetime,
    ) -> List[DublinMeta]:
        return (
            db.query(self.model.journey_id)
            .distinct()
            .filter(DublinMeta.time_frame >= start_date)
            .filter(DublinMeta.time_frame <= end_date)
            .all()
        )

    def get_traj_by_journey_date(
        self, db: Session, *, journey_id: str, start_date: datetime, end_date: datetime,
    ) -> List[DublinMeta]:
        return (
            db.query(self.model.trajectory_id)
            .distinct()
            .filter(DublinMeta.journey_id == journey_id)
            .filter(DublinMeta.time_frame >= start_date)
            .filter(DublinMeta.time_frame <= end_date)
            .all()
        )

    def get_all_metas(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[DublinMeta]:
        return db.query(self.model).all()

    def get_traj_by_turno(self, db: Session, *, turno: str):
        query = db.query(DublinMeta.trajectory_id).distinct()
        turno_dict = {
            "MANHA": [6, 12],
            "TARDE": [12, 18],
            "NOITE": [18, 24],
            "MADRUGADA": [0, 6],
        }
        query = query.filter(
            extract("hour", DublinMeta.first_instant) >= turno_dict[turno][0]
        ).filter(extract("hour", DublinMeta.first_instant) < turno_dict[turno][1])
        return query.all()


dublin_meta = CRUDDublinMeta(DublinMeta)

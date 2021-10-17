#!/usr/bin/env ipython

from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.dublin_model import DublinModel
from app.schemas.dublin_model import DublinModelCreate, DublinModelUpdate


class CRUDDublinModel(CRUDBase[DublinModel, DublinModelCreate, DublinModelUpdate]):
    def get_predictions(
            self, db: Session, *, trajectory_id: int = None, routes: int = None
    ) -> List[DublinModel]:
        return (
            db.query(self.model)
            .filter(
                (DublinModel.trajectory_id == trajectory_id)
                & (DublinModel.routes == routes))
#            .offset(0)
#            .limit(100)
            .all()
        )


dublin_model = CRUDDublinModel(DublinModel)

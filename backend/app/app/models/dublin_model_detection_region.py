#!/usr/bin/env ipython
from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class DublinModelDetectionRegion(Base):
    index = Column(Integer, primary_key=True)
    model = Column(String)
    route = Column(Integer)
    trajectory_id = Column(Integer)
    anom_predictions = Column(String)
    anom_true = Column(String)

#!/usr/bin/env ipython
from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class DublinPredictionRegion(Base):
    index = Column(Integer, primary_key=True)
    filename = Column(String)
    rota = Column(Integer)
    trajectory_id = Column(Integer)
    anon_predictions = Column(String)
    true_anon = Column(String)

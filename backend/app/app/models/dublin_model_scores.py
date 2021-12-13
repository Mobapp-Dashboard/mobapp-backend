#!/usr/bin/env ipython
from sqlalchemy import Column, Integer, Numeric, String

from app.db.base_class import Base


class DublinModelScores(Base):
    index = Column(Integer, primary_key=True)
    route = Column(Integer)
    trajectory_id = Column(Integer)
    model = Column(String)
    scores = Column(Numeric)

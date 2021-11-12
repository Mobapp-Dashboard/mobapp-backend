#!/usr/bin/env ipython

from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Numeric

from app.db.base_class import Base


class DublinModelPoints(Base):
    index = Column(Integer, primary_key=True)
    trajectory_id = Column(Integer)
    rota = Column(Integer)
    lat = Column(Numeric)
    lng = Column(Numeric)

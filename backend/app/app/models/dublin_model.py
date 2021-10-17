#!/usr/bin/env ipython

from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Numeric

from app.db.base_class import Base


class DublinModel(Base):
    index = Column(Integer, primary_key=True)
    trajectory_id = Column(Integer)
    predicted =  Column(Integer)
    input_token = Column(Integer)
    routes = Column(Integer)
    lat = Column(Numeric)
    lng = Column(Numeric)

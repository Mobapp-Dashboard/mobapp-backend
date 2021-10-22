#!/usr/bin/env ipython

from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, Integer, Numeric, String

from app.db.base_class import Base

class DublinPoints(Base):
    id = Column(Integer, primary_key=True, index=True)
    # trajectory_id = Column(Integer, ForeignKey("dublinmeta.trajectory_id"))
    trajectory_id = Column(Integer)
    instant = Column(DateTime)
    lat = Column(Numeric)
    lng = Column(Numeric)
    lat_mercator = Column(Numeric)
    lng_mercator = Column(Numeric)
    speed = Column(Numeric)
    acceleration = Column(Numeric)
    position = Column(Integer)
    delta_dist = Column(Numeric)
    delta_time = Column(Numeric)
    bearing = Column(Numeric)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    hour = Column(Integer)
    minute = Column(Integer)
    stop_labels = Column(Integer)
    day_moment = Column(String)

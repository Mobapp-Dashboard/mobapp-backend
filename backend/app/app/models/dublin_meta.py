from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class DublinMeta(Base):
    trajectory_id = Column(Integer, primary_key=True, index=True)
    # line_id =  Column(Integer)
    journey_id = Column(String)
    time_frame = Column(DateTime)
    vehicle_journey_id = Column(Integer)
    operator = Column(String)
    vehicle_id = Column(Integer)
    # trajectory_size = Column(Integer)
    first_lat = Column(Numeric)
    last_lat = Column(Numeric)
    first_lng = Column(Numeric)
    last_lng = Column(Numeric)
    first_instant = Column(DateTime)
    last_instant = Column(DateTime)
    # route = Column(String)
    # outlier = Column(Boolean())

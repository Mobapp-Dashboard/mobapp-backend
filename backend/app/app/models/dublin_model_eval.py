from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String

from app.db.base_class import Base


class DublinModelEval(Base):
    index = Column(Integer, primary_key=True)
    model = Column(String)
    route = Column(Integer)
    precision = Column(Numeric)
    recall = Column(Numeric)
    threshold = Column(Numeric)

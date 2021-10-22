from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String

from app.db.base_class import Base


class DublinEvalModels(Base):
    index = Column(Integer, primary_key=True)
    filename = Column(String)
    rota = Column(Integer)
    auc = Column(Numeric)
    max_f1 = Column(Numeric)
    f1_thr = Column(Numeric)
    precision = Column(Numeric)
    recall = Column(Numeric)
    threshold = Column(Numeric)

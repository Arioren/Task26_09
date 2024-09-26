from config.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Target(Base):
    __tablename__ = "targets"
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_priority = Column(Integer)
    target_industry = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.city_id'), nullable=False)
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'), nullable=False)

    city = relationship("City", back_populates="targets")
    type = relationship("TargetType", back_populates="targets")












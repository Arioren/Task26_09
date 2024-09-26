from config.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Target(Base):
    __tablename__ = "Targets"
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_priority = Column(Integer)
    target_industry = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'))
    target_type_id = Column(Integer, ForeignKey('type.id'))

    city = relationship("City", back_populates="Targets")
    type = relationship("Type", back_populates="Targets")












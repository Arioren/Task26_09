from config.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Type(Base):
    __tablename__ = "TargetTypes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_id = Column(String(100), unique=True, nullable=False)

    Targets = relationship("Targets", back_populates="type")





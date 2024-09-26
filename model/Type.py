from config.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class TargetType(Base):
    __tablename__ = "targettypes"
    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String(100), unique=True, nullable=False)

    targets = relationship("Target", back_populates="type")





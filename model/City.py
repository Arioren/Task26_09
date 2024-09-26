from config.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = "Cities"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(100), unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey('Countries.id'))
    latitude = Column(Float)
    longitude = Column(Float)

    country = relationship("Country", back_populates="cities")
    targets = relationship("Target", back_populates="city")



from config.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(100), unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.country_id'))
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)

    country = relationship("Country", back_populates="cities")
    targets = relationship("Target", back_populates="city")



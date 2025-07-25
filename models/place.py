#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel, Base):
    """ A place to stay """
    city_id = Column(String(60), ForeignKey("cities.id"), nullable= False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable = False)
    name = Column(String(128), nullable = False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable = False, default = 0)
    number_bathrooms = Column(Integer, nullable = False, default = 0)
    max_guest = Column(Integer, nullable = False, default = 0)
    price_by_night = Column(Integer, nullable = False, default = 0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []



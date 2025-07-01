#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(128), nallable = False, ForeignKey(" states.id)")
    name = Column(String(128), nullable = False)
    places = relationship("Places", back_populates = "cities")

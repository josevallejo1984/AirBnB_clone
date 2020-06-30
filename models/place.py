#!/usr/bin/python3
"""New class inherit from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place that inherit from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = None
    number_bathrooms = None
    price_by_night: None
    latitude: None
    longitude: None
    amenity_ids = []

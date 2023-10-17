#!/usr/bin/python3
"""script define the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representing an amenity.
    Attribute:
        name (str): The name of the amenity.
    """

    name = ""

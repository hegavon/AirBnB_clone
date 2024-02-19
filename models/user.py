#!/usr/bin/python3
"""
Module User class
"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    '''Inherits from the Parent class(BaseModel)'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

#!/usr/bin/python3
#base.py
"""Defines a base model class"""
import csv
import json
import turtle

class Base:
    """Represent the base model.
    
    Serves as the foundational framework for all other classes within this project.
    
    Attributes:
        __nb_objects (int): Account for the number of instantiated bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base.
        
        Args:
            is (int): The id of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects



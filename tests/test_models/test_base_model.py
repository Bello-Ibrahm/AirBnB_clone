#!/usr/bin/python3
"""Define unittests for the models/base_model.py"""
import os
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Unittests for testing ation of the BaseModel"""
    def __init__(self):
        """Init the test class of BaseModel"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_no_args(self):
        """Unittest for testing instantiation with no args"""
        self.assertEqual(BaseModel, type(BaseModel()))



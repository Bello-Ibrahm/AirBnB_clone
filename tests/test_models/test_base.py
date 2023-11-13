#!/usr/bin/python3
"""Define unittests for the models/base_model.py"""
import os
import unittest
import models
import json
from uuid import UUID
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing ation of the BaseModel"""

    def test_setUp(self):
        """The setup method of the test class"""
        pass

    def test_tearDown(self):
        """teardown method of the class test"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_no_args(self):
        """Unittest for testing instantiation with no args"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_pub_id_str(self):
        """Unittest if public id is a string"""
        self.assertEqual(str, type(BaseModel().id))


if __name__ == "__main__":
    unittest.main()

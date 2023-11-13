#!/usr/bin/python3
"""Defines unittests for Amenity Model class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class test_Amenity_Test(unittest.TestCase):
    """Tests for Amenity class"""

    def test_Amenity_from_Base(self):
        """Tests if Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_Amenity_attributes(self):
        """Tests for Amenity Attributes"""
        amenity = Amenity()
        self.assertTrue("name" in amenity.__dir__())

    def test_Amentiy_type(self):
        """Tests for Amenity type"""
        amenity = Amenity()
        amenity_name = getattr(amenity, "name")
        self.assertIsInstance(amenity_name, str)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Defines unittests for Place Model class"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class test_Place_Test(unittest.TestCase):
    """Tests for Place class"""

    def test_Place_from_Base(self):
        """Tests if Place inherits from BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_Place_attributes(self):
        """Tests for Place attributes"""
        place = Place()
        self.assertTrue("city_id" in place.__dir__())
        self.assertTrue("user_id" in place.__dir__())
        self.assertTrue("name" in place.__dir__())
        self.assertTrue("description" in place.__dir__())
        self.assertTrue("number_rooms" in place.__dir__())
        self.assertTrue("number_bathrooms" in place.__dir__())
        self.assertTrue("max_guest" in place.__dir__())
        self.assertTrue("price_by_night" in place.__dir__())
        self.assertTrue("latitude" in place.__dir__())
        self.assertTrue("longitude" in place.__dir__())
        self.assertTrue("amenity_ids" in place.__dir__())


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Defines unittests for Review Model class"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class test_Review_Test(unittest.TestCase):
    """Tests for Review class"""

    def test_Review_from_Base(self):
        """Tests if Review inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_Review_attributes(self):
        """Tests for Review attributes"""
        review = Review()
        self.assertTrue("place_id" in review.__dir__())
        self.assertTrue("user_id" in review.__dir__())
        self.assertTrue("text" in review.__dir__())

    def test_review_type(self):
        """Tests for Review type"""
        review = Review()
        place_id = getattr(review, "place_id")
        user_id = getattr(review, "user_id")
        text = getattr(review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)


if __name__ == "__main__":
    unittest.main()

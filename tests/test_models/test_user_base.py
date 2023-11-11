#!/usr/bin/python3
"""Defines unittests for User Model class"""
import unittest
from models.base_model import BaseModel
from models.user import User
import sys
import datetime


class User_Test(unittest.TestCase):
    """Tests for User class"""

    def User_from_Base(self):
        """Tests if User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def User_attributes(self):
        """Tests for Users attributes"""

        user = User()
        self.assertTrue("email" in user.__dir__())
        self.assertTrue("password" in user.__dir__())
        self.assertTrue("first_name" in user.__dir__())
        self.assertTrue("last_name" in user.__dir__())

    def email_type(self):
        """Tests for email type"""
        user = User()
        email_type = getattr(user, "email")
        self.assertIsInstance(email_type, str)


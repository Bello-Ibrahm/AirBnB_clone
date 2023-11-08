#!/usr/bin/python3
"""Module that instantiates an instance of the storage to be used"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

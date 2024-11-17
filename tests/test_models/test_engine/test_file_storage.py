#!/usr/bin/python3
"""Unittest for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test Suite"""

    def setUp(self):
        """Setup instances of FileStorage class for tests"""
        self.storage = FileStorage()
        self.instance = BaseModel()

    def test_all(self):
        """Test ``all`` method"""
        instances = self.storage.all()
        for instance in instances.keys():
            cls_name = instances[instance].__class__.__name__
            self.assertEqual(instances[instance].__class__.__name__, cls_name)

    def test_new(self):
        """Test ``new`` method"""
        new_inst = BaseModel()
        self.storage.new(new_inst)
        key = f"{new_inst.__class__.__name__}.{new_inst.id}"
        self.assertIn(key, self.storage.all().keys())

    def test_save(self):
        """Test ``save`` method"""
        new_inst = BaseModel()
        key = f"{new_inst.__class__.__name__}.{new_inst.id}"
        new_inst.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all().keys())

    def test_reload(self):
        """Test ``reload`` method"""
        new_inst = BaseModel()
        key = f"{new_inst.__class__.__name__}.{new_inst.id}"
        new_inst.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all().keys())

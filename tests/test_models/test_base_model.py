#!/usr/bin/python3
"""Unittests for BaseModel class"""
from models.base_model import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """Test Suite"""

    def setUp(self):
        """Setup instances of BaseModel class for tests"""
        self.obj_dict = {"id": "7ae56a93-0712-43db-bd33-14d63aa60184",
                         "created_at": "2024-11-12T16:13:19.651327",
                         "updated_at": "2024-11-12T16:13:19.651371"
                         }
        self.obj_no_dict = BaseModel()
        self.obj_w_dict = BaseModel(**self.obj_dict)

    def test_init_no_dict(self):
        """Tests BaseModel initialization without a dictionary"""
        self.assertEqual(self.obj_no_dict, self.obj_no_dict)
        self.assertEqual(self.obj_no_dict.id, self.obj_no_dict.id)
        self.assertEqual(self.obj_no_dict.__class__,
                         self.obj_no_dict.__class__)
        self.assertEqual(self.obj_no_dict.created_at,
                         self.obj_no_dict.created_at)
        self.assertEqual(self.obj_no_dict.updated_at,
                         self.obj_no_dict.updated_at)

    def test_init_dict(self):
        """Tests BaseModel initialization without a dictionary"""
        c_key = "created_at"
        u_key = "updated_at"
        self.assertEqual(self.obj_w_dict, self.obj_w_dict)
        self.assertEqual(self.obj_w_dict.id,
                         "7ae56a93-0712-43db-bd33-14d63aa60184")
        self.assertEqual(self.obj_w_dict.__class__,
                         self.obj_w_dict.__class__)
        self.assertEqual(self.obj_w_dict.created_at,
                         self.obj_w_dict.created_at)
        self.assertEqual(self.obj_w_dict.updated_at,
                         self.obj_w_dict.updated_at)
        self.assertEqual(self.obj_w_dict.created_at,
                         datetime.datetime.fromisoformat(self.obj_dict[c_key]))
        self.assertEqual(self.obj_w_dict.updated_at,
                         datetime.datetime.fromisoformat(self.obj_dict[u_key]))
        self.assertEqual(type(self.obj_w_dict), BaseModel)
        self.assertEqual(type(self.obj_w_dict.created_at), datetime.datetime)
        self.assertEqual(type(self.obj_w_dict.updated_at), datetime.datetime)

    def test_obj_no_dict_str(self):
        """Test string representation of a BaseModel object"""
        out = f"""[{self.obj_no_dict.__class__.__name__}] \
({self.obj_no_dict.id}) {self.obj_no_dict.__dict__}"""
        self.assertEqual(str(self.obj_no_dict), out)

    def test_obj_w_dict_str(self):
        """Test string representation of a BaseModel object"""
        out = f"""[{self.obj_w_dict.__class__.__name__}] \
({self.obj_w_dict.id}) {self.obj_w_dict.__dict__}"""
        self.assertEqual(str(self.obj_w_dict), out)

    def test_obj_no_dict_to_dict(self):
        """Test dictionary representation of a BaseModel object"""
        obj_dict = {
                    "id": self.obj_no_dict.id,
                    "created_at": self.obj_no_dict.created_at.isoformat(),
                    "updated_at": self.obj_no_dict.updated_at.isoformat(),
                    "__class__": "BaseModel"
                    }
        self.assertEqual(self.obj_no_dict.to_dict(), obj_dict)

    def test_obj_w_dict_to_dict(self):
        """Test dictionary representation of a BaseModel object"""
        obj_dict = {
                    "id": "7ae56a93-0712-43db-bd33-14d63aa60184",
                    "created_at": self.obj_w_dict.created_at.isoformat(),
                    "updated_at": self.obj_w_dict.updated_at.isoformat(),
                    "__class__": "BaseModel",
                    }
        self.assertEqual(self.obj_w_dict.to_dict(), obj_dict)

    def test_save(self):
        """Test save method"""
        updated = self.obj_no_dict.updated_at
        self.obj_no_dict.save()
        self.assertNotEqual(updated, self.obj_no_dict.updated_at)


if __name__ == "__main__":
    unittest.main()

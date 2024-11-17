#!/usr/bin/python3
"""Unittests for Place class"""
from models.place import Place
import datetime
import unittest


class TestPlace(unittest.TestCase):
    """Test Suite"""

    def setUp(self):
        """Setup instances of Place"""
        self.obj_dict = {"id": "7ae56a93-0712-43db-bd33-14d63aa60184",
                         "created_at": "2024-11-12T16:13:19.651327",
                         "updated_at": "2024-11-12T16:13:19.651371",
                         "name": "Villa",
                         "state_id": "f281a134-395e-4027-b853-eb5b85959e6b",
                         "city_id": "ec28a5da-3743-4874-9f6a-6aa73549e343",
                         "user_id": "d0425e09-303a-478a-a6b7-803526d1afb2",
                         "description": "Two bedroom self-contained",
                         "number_rooms": 2,
                         "number_bathrooms": 1,
                         "max_guests": 2,
                         "price_by_night": 200,
                         "latitude": 0.5,
                         "longitude": 1.2,
                         "amenity_ids": []
                         }
        self.obj_no_dict = Place()
        self.obj_w_dict = Place(**self.obj_dict)

    def test_init_no_dict(self):
        """Tests Place initialization without a dictionary"""
        self.assertEqual(self.obj_no_dict, self.obj_no_dict)
        self.assertEqual(self.obj_no_dict.id, self.obj_no_dict.id)
        self.assertEqual(self.obj_no_dict.__class__, Place)
        self.assertEqual(self.obj_no_dict.created_at,
                         self.obj_no_dict.created_at)
        self.assertEqual(self.obj_no_dict.updated_at,
                         self.obj_no_dict.updated_at)

    def test_init_dict(self):
        """Tests Place initialization without a dictionary"""
        c_key = "created_at"
        u_key = "updated_at"
        self.assertEqual(self.obj_w_dict, self.obj_w_dict)
        self.assertEqual(self.obj_w_dict.id,
                         "7ae56a93-0712-43db-bd33-14d63aa60184")
        self.assertEqual(self.obj_w_dict.__class__, Place)
        self.assertEqual(self.obj_w_dict.name, "Villa")
        self.assertEqual(self.obj_w_dict.state_id,
                         "f281a134-395e-4027-b853-eb5b85959e6b")
        self.assertEqual(self.obj_w_dict.city_id,
                         "ec28a5da-3743-4874-9f6a-6aa73549e343")
        self.assertEqual(self.obj_w_dict.user_id,
                         "d0425e09-303a-478a-a6b7-803526d1afb2")
        self.assertEqual(self.obj_w_dict.description,
                         "Two bedroom self-contained")
        self.assertEqual(self.obj_w_dict.number_rooms, 2)
        self.assertEqual(self.obj_w_dict.number_bathrooms, 1)
        self.assertEqual(self.obj_w_dict.max_guests, 2)
        self.assertEqual(self.obj_w_dict.price_by_night, 200)
        self.assertEqual(self.obj_w_dict.latitude, 0.5)
        self.assertEqual(self.obj_w_dict.longitude, 1.2)
        self.assertEqual(self.obj_w_dict.amenity_ids, [])
        self.assertEqual(type(self.obj_w_dict.number_rooms), int)
        self.assertEqual(type(self.obj_w_dict.number_bathrooms), int)
        self.assertEqual(type(self.obj_w_dict.max_guests), int)
        self.assertEqual(type(self.obj_w_dict.price_by_night), int)
        self.assertEqual(type(self.obj_w_dict.latitude), float)
        self.assertEqual(type(self.obj_w_dict.longitude), float)
        self.assertEqual(type(self.obj_w_dict.amenity_ids), list)
        self.assertEqual(self.obj_w_dict.created_at,
                         datetime.datetime.fromisoformat(self.obj_dict[c_key]))
        self.assertEqual(self.obj_w_dict.updated_at,
                         datetime.datetime.fromisoformat(self.obj_dict[u_key]))
        self.assertEqual(type(self.obj_w_dict), Place)
        self.assertEqual(type(self.obj_w_dict.created_at), datetime.datetime)
        self.assertEqual(type(self.obj_w_dict.updated_at), datetime.datetime)

    def test_obj_no_dict_str(self):
        """Test string representation of a Place object"""
        out = f"""[{self.obj_no_dict.__class__.__name__}] \
({self.obj_no_dict.id}) {self.obj_no_dict.__dict__}"""
        self.assertEqual(str(self.obj_no_dict), out)

    def test_obj_w_dict_str(self):
        """Test string representation of a Place object"""
        out = f"""[Place] (7ae56a93-0712-43db-bd33-14d63aa60184) \
{self.obj_w_dict.__dict__}"""
        self.assertEqual(str(self.obj_w_dict), out)

    def test_obj_no_dict_to_dict(self):
        """Test dictionary representation of a Place object"""
        obj_dict = {
                    "id": self.obj_no_dict.id,
                    "created_at": self.obj_no_dict.created_at.isoformat(),
                    "updated_at": self.obj_no_dict.updated_at.isoformat(),
                    "__class__": "Place"
                    }
        self.assertEqual(self.obj_no_dict.to_dict(), obj_dict)

    def test_obj_w_dict_to_dict(self):
        """Test dictionary representation of a Place object"""
        obj_dict = {
                    "id": "7ae56a93-0712-43db-bd33-14d63aa60184",
                    "created_at": self.obj_w_dict.created_at.isoformat(),
                    "updated_at": self.obj_w_dict.updated_at.isoformat(),
                    "__class__": "Place",
                    "name": "Villa",
                    "state_id": "f281a134-395e-4027-b853-eb5b85959e6b",
                    "city_id": "ec28a5da-3743-4874-9f6a-6aa73549e343",
                    "user_id": "d0425e09-303a-478a-a6b7-803526d1afb2",
                    "description": "Two bedroom self-contained",
                    "number_rooms": 2,
                    "number_bathrooms": 1,
                    "max_guests": 2,
                    "price_by_night": 200,
                    "latitude": 0.5,
                    "longitude": 1.2,
                    "amenity_ids": []
                    }
        self.assertEqual(self.obj_w_dict.to_dict(), obj_dict)

    def test_save(self):
        """Test save method"""
        updated = self.obj_no_dict.updated_at
        self.obj_no_dict.save()
        self.assertNotEqual(updated, self.obj_no_dict.updated_at)


if __name__ == "__main__":
    unittest.main()

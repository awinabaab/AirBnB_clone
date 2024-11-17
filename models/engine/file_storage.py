#!/usr/bin/python3
"""File Storage Module"""

import json
from importlib import import_module


class FileStorage:
    """A class representing FileStorage"""

    __file_path = "file.json"
    __objects = {}

    class_module = {
            "BaseModel": "models.base_model",
            "User": "models.user",
            "Place": "models.place",
            "State": "models.state",
            "City": "models.city",
            "Amenity": "models.amenity",
            "Review": "models.review"
            }

    @classmethod
    def get_objects(cls):
        """Getter method that returns items in ``__objects``"""
        return cls.__objects

    def all(self):
        """Returns the dictionary ``__objects``"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in ``__objects`` the obj with key ``obj_class_name.id``"""
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serializes ``__objects`` to the JSON file"""
        obj_dictionary = {}
        for obj_key, obj in FileStorage.__objects.items():
            obj_dictionary[obj_key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dictionary, f)

    def reload(self):
        """Deserializes the JSON file to ``__objects``"""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dictionary = json.load(f)
            for obj_key, obj in obj_dictionary.items():
                class_name = obj_key.split(".")[0]
                module_path = self.class_module.get(class_name)
                if module_path:
                    module = import_module(module_path)
                    cls = getattr(module, class_name)
                    FileStorage.__objects[obj_key] = cls(**obj)
        except Exception:
            pass

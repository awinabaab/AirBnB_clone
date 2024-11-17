#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class"""

    def setUp(self):
        """Set up resources before each test"""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up resources after each test"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_instance_creation(self):
        """Test that FileStorage is instantiated properly"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_all_returns_dict(self):
        """Test that 'all' method returns a dictionary"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new_adds_object(self):
        """Test that 'new' method adds an object to storage"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """Test that 'save' creates a JSON file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_populates_storage(self):
        """Test that 'reload' repopulates objects from file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Create a new FileStorage instance to simulate reloading
        new_storage = FileStorage()
        new_storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, new_storage.all())

    def test_empty_reload_does_not_crash(self):
        """Test that 'reload' does not crash on an empty file"""
        open(self.file_path, "w").close()  # Create an empty file
        try:
            self.storage.reload()
            self.assertTrue(True)  # No exceptions raised
        except Exception as e:
            self.fail(f"Reload crashed with an empty file: {e}")

    def test_save_and_reload(self):
        """Test save and reload workflow"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, obj.id)

    def test_save_overwrites_file(self):
        """Test that 'save' overwrites the existing file"""
        obj1 = BaseModel()
        obj1.save()
        with open(FileStorage._FileStorage__file_path, 'r') as file:
            content = file.read()
        self.assertIn(obj1.id, content)

        obj2 = BaseModel()
        obj2.save()
        with open(FileStorage._FileStorage__file_path, 'r') as file:
            content = file.read()
        self.assertIn(obj2.id, content)
        self.assertIn(obj1.id, content)

    def test_new_raises_error_with_invalid_input(self):
        """Test 'new' raises an error if input is not BaseModel"""
        with self.assertRaises(AttributeError):
            self.storage.new(None)

    def test_reload_with_corrupted_file(self):
        """Test 'reload' handles a corrupted JSON file gracefully"""
        with open(self.file_path, "w") as f:
            f.write("corrupted content")
        try:
            self.storage.reload()
        except Exception as e:
            self.fail(f"Reload crashed with corrupted file: {e}")

    def test_reload_with_missing_file(self):
        """Test 'reload' gracefully handles a missing file"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        try:
            self.storage.reload()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Reload crashed with missing file: {e}")


if __name__ == "__main__":
    unittest.main()

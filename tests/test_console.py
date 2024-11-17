import unittest
import os
import sys
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for HBNBCommand"""

    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()
        self.stdout = StringIO()
        sys.stdout = self.stdout
        storage.reload()

    def tearDown(self):
        """Clean up after each test"""
        sys.stdout = sys.__stdout__
        self.stdout.close()
        if os.path.exists("file.json"):
            os.remove("file.json")

    def get_output(self):
        """Helper to get the output from stdout"""
        return self.stdout.getvalue().strip()

    def test_quit(self):
        """Test the 'quit' command"""
        self.assertTrue(self.console.onecmd("quit"))

    def test_eof(self):
        """Test the 'EOF' command"""
        self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        """Test empty line does nothing"""
        self.assertFalse(self.console.onecmd(""))

    def test_create_missing_class(self):
        """Test 'create' with no class name"""
        self.console.onecmd("create")
        self.assertEqual(self.get_output(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test 'create' with invalid class name"""
        self.console.onecmd("create InvalidClass")
        self.assertEqual(self.get_output(), "** class doesn't exist **")

    def test_create_valid_class(self):
        """Test 'create' with a valid class name"""
        self.console.onecmd("create BaseModel")
        output = self.get_output()
        self.assertTrue(len(output) > 0)  # An ID is printed
        key = f"BaseModel.{output}"
        objects = storage.all()
        self.assertIn(key, objects)

    def test_show_missing_class(self):
        """Test 'show' with no class name"""
        self.console.onecmd("show")
        self.assertEqual(self.get_output(), "** class name missing **")

    def test_show_missing_id(self):
        """Test 'show' with missing ID"""
        self.console.onecmd("show BaseModel")
        self.assertEqual(self.get_output(), "** instance id missing **")

    def test_show_invalid_class(self):
        """Test 'show' with invalid class name"""
        self.console.onecmd("show InvalidClass 1234")
        self.assertEqual(self.get_output(), "** class doesn't exist **")

    def test_show_nonexistent_instance(self):
        """Test 'show' with a nonexistent instance"""
        self.console.onecmd("show BaseModel 1234")
        self.assertEqual(self.get_output(), "** no instance found **")

    def test_show_valid_instance(self):
        """Test 'show' with a valid instance"""
        obj = BaseModel()
        obj.save()
        self.console.onecmd(f"show BaseModel {obj.id}")
        self.assertIn(str(obj), self.get_output())

    def test_destroy_missing_class(self):
        """Test 'destroy' with no class name"""
        self.console.onecmd("destroy")
        self.assertEqual(self.get_output(), "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test 'destroy' with invalid class name"""
        self.console.onecmd("destroy InvalidClass 1234")
        self.assertEqual(self.get_output(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test 'destroy' with missing ID"""
        self.console.onecmd("destroy BaseModel")
        self.assertEqual(self.get_output(), "** instance id missing **")

    def test_destroy_nonexistent_instance(self):
        """Test 'destroy' with nonexistent instance"""
        self.console.onecmd("destroy BaseModel 1234")
        self.assertEqual(self.get_output(), "** no instance found **")

    def test_destroy_valid_instance(self):
        """Test 'destroy' with a valid instance"""
        obj = BaseModel()
        obj.save()
        self.console.onecmd(f"destroy BaseModel {obj.id}")
        self.assertEqual(self.get_output(), "")
        objects = storage.all()
        self.assertNotIn(f"BaseModel.{obj.id}", objects)

    def test_all_no_class(self):
        """Test 'all' with no class name"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()
        self.console.onecmd("all")
        output = self.get_output()
        self.assertIn(str(obj1), output)
        self.assertIn(str(obj2), output)

    def test_all_with_class(self):
        """Test 'all' with a specific class name"""
        obj = BaseModel()
        obj.save()
        self.console.onecmd("all BaseModel")
        output = self.get_output()
        self.assertIn(str(obj), output)

    def test_all_invalid_class(self):
        """Test 'all' with an invalid class name"""
        self.console.onecmd("all InvalidClass")
        self.assertEqual(self.get_output(), "** class doesn't exist **")

    def test_update_missing_class(self):
        """Test 'update' with no class name"""
        self.console.onecmd("update")
        self.assertEqual(self.get_output(), "** class name missing **")

    def test_update_invalid_class(self):
        """Test 'update' with an invalid class name"""
        self.console.onecmd("update InvalidClass 1234 attr value")
        self.assertEqual(self.get_output(), "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test 'update' with missing ID"""
        self.console.onecmd("update BaseModel")
        self.assertEqual(self.get_output(), "** instance id missing **")

    def test_update_nonexistent_instance(self):
        """Test 'update' with nonexistent instance"""
        self.console.onecmd("update BaseModel 1234 attr value")
        self.assertEqual(self.get_output(), "** no instance found **")

    def test_update_missing_attribute(self):
        """Test 'update' with missing attribute name"""
        obj = BaseModel()
        obj.save()
        self.console.onecmd(f"update BaseModel {obj.id}")
        self.assertEqual(self.get_output(), "** attribute name missing **")

    def test_update_missing_value(self):
        """Test 'update' with missing value"""
        obj = BaseModel()
        obj.save()
        self.console.onecmd(f"update BaseModel {obj.id} name")
        self.assertEqual(self.get_output(), "** value missing **")

    def test_update_valid_attribute(self):
        """Test 'update' with a valid attribute"""
        obj = BaseModel()
        obj.save()
        self.console.onecmd(f'update BaseModel {obj.id} name "John Doe"')
        obj = storage.all()[f"BaseModel.{obj.id}"]
        self.assertEqual(obj.name, "John Doe")


if __name__ == "__main__":
    unittest.main()

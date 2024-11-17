#!/usr/bin/python3
"""Console Module"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """Entry point to command interpreter"""
    prompt = '(hbnb) '
    defined_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }
    class_list = list(defined_classes.keys())

    def do_quit(self, _):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, _):
        """Exits the program
        """
        return True

    def emptyline(self):
        """Executes nothing with emptyline + Enter"""
        pass

    def do_create(self, arg):
        """Creates a new class instance, saves it to JSON file and prints id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.defined_classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of instance based on class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = f"{args[0]}.{args[1]}"
        objects = FileStorage.get_objects()
        if obj_key not in objects:
            print("** no instance found **")
            return
        else:
            print(objects[obj_key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = f"{args[0]}.{args[1]}"
        objects = FileStorage.get_objects()
        if obj_key not in objects:
            print("** no instance found **")
            return
        else:
            del objects[obj_key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        """
        instance_list = []
        objects = FileStorage.get_objects()
        if arg:
            args = arg.split()
            if args[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
                return
            else:
                for obj_key, obj in objects.items():
                    if obj.__class__.__name__ == args[0]:
                        instance_list.append(str(obj))
        else:
            for obj_key, obj in objects.items():
                instance_list.append(str(obj))
        print(instance_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = f"{args[0]}.{args[1]}"
        objects = FileStorage.get_objects()
        if obj_key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objects[obj_key]
        attribute_name = args[2].strip('"').strip("'")
        attribute = args[3].strip('"').strip("'")
        if hasattr(obj, attribute_name):
            attribute_type = type(getattr(obj, attribute_name))
            attribute = attribute_type(attribute)
        else:
            if attribute.isdigit():
                attribute = int(attribute)
            else:
                try:
                    attribute = float(attribute)
                except ValueError:
                    pass
        setattr(obj, attribute_name, attribute)
        obj.save()

    def default(self, line):
        """Retrieves all instances of a class by using dot notation
        """
        class_name = None
        for char in line:
            if char == ".":
                args = line.split(".", 1)
                command = args[1]
                if command[-2:] == "()":
                    command = command[:-2]
                    parameters = None
                elif "(" in command and ")" in command:
                    inputs = command.split("(", 1)
                    parameters = inputs[1].rstrip(")")
                    command = inputs[0]
                else:
                    break
                class_name = args[0]
                break
        if class_name is None:
            print(f"*** Unknown syntax: {line}")
            return
        if command == "all":
            self.do_all(class_name)
        if command == "count":
            self.count(class_name)
        if command == "show":
            if parameters is None:
                self.do_show(class_name)
                return
            parameters = parameters.strip('"')
            arg = f"{class_name} {parameters}"
            self.do_show(arg)
        if command == "destroy":
            if parameters is None:
                self.do_destroy(class_name)
                return
            parameters = parameters.strip('"')
            arg = f"{class_name} {parameters}"
            self.do_destroy(arg)
        if command == "update":
            if parameters is None:
                self.do_update(class_name)
                return
            key_value_list = []
            components = parameters.split(",", 1)
            id_component = components[0]
            id_component = id_component.strip('"')
            id_component = id_component.strip("'")
            key_value_component = components[1].strip(" ")
            if key_value_component[0] == "{":
                key_value_list = self.key_val_list(key_value_component)
            else:
                key_value_list.append(key_value_component.replace(",", ""))
            kv_list = []
            for pair in key_value_list:
                if pair[0] == '"':
                    kv_list.append(pair.replace('"', '', 2))
                elif pair[0] == "'":
                    kv_list.append(pair.replace("'", "", 2))
                else:
                    kv_list.append(pair)
            key_value_list = kv_list.copy()
            for pair in key_value_list:
                arg = f"{class_name} {id_component} {pair}"
                self.do_update(arg)

    def count(self, class_name):
        """Retrieves the number of instances of a class
        """
        instance_list = []
        objects = FileStorage.get_objects()
        for obj_key, obj in objects.items():
            if obj.__class__.__name__ == class_name:
                instance_list.append(str(obj))
        print(len(instance_list))

    def key_val_list(self, dictionary):
        """Returns a list of key, value pairs from a dictionary
        """
        dictionary = dictionary.strip("{}")
        key_value_list = dictionary.split(",")
        kv_list = []
        for pair in key_value_list:
            kv_list.append(pair.replace(":", ""))
        key_value_list = kv_list.copy()
        return key_value_list


if __name__ == '__main__':
    HBNBCommand().cmdloop()

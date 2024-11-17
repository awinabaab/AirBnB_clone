# AirBnB Clone - The Console

Welcome to our AirBnB Clone - The Console project. This is the first step towards building our first full web application with ALXSE: The AirBnB clone.

Coming after this project will be HTML/CSS templating, database storage, API, front-end integration etc.

The focus of this project is outlined below. The project is made of of a series of tasks that culminate together into a full-on console application.
Each task is linked and will help to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Features
- Command interpreter (using Python cmd module)
- Command interpreter (the console) will help to manage the objects of the project
    - Create a new object (ex: a new User or a new Place)
    - Retrieve an object from a file, a database etc…
    - Do operations on objects (count, compute stats, etc…)
    - Update attributes of an object
    - Destroy an object

## Getting Started

### Execution
In interactive mode:
```bash
$ ./console.py
```
In non-interactive mode:
```bash
$ echo <command> | ./console.py
```
### Example commands
Here are a few basic commands you can try with the console:
- `help` - List of documented commands.
- `create <class_name>` - Create new instance of class.
- `quit` - Exit program.
- `all` - Print string representation of all instances based or not on class name.
### Project Details
- Language: Python
- Standard: Pycodestyle (version 2.8.\*)
- *Warnings: All enabled for best practices and error prevention.*

<br>

By: [Emmanuel K. Tettey](https://github.com/anuelt2) and [Abdul-Mumin Awinaba](https://github.com/awinabaab)

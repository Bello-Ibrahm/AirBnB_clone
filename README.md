# HBNB - The console

This repository contains the initial a project to build a clone of the AirBnB website. This stage implements a console, to manage program data. Console commands allow the user to CRUD (Create, Read, Update, and Destroy) objects, as well as manage file storage.
## General usage:

1. Clone the repository
2. Change directory to AirBnB_clone
3.  to run the app ./console.py e.g `/AirBnB_clone# ./console.py`

### To read command usages: type help followed by the command
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help create
Create a class of any type
[Usage]: create <className>

(hbnb) help destroy
Destroys an individual instance of a class
[Usage]: destroy <className> <objectId>

(hbnb) help all
Shows all objects, or all of a class
[Usage]: all <className>

(hbnb) help update
Updates an object with new information
[Usage]: update <className> <id> <attrName> <attVal>
```

## Test commands
Single testing
`python3 -m unittest tests/test_models/test_base_model.py`
`python3 -m unittest tests/test_models/test_user.py`
`python3 -m unittest -v tests.test_models.test_city`

General testing
`python3 -m unittest discover tests`

Module Documentation
`python3 -c 'print(__import__("my_module").__doc__)'`

Classes documentation 
`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`

Functions/Methods documentation
`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and 
`python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`

# AUTHORS
-  Bello Ibrahim

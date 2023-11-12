#!/usr/bin/python3
"""Console module"""
import cmd
import sys
import models
import shlex
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB"""

    # Check for interactive/non-interactive mode
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    model_list = ["BaseModel",
                  "Amenity",
                  "State",
                  "City",
                  "Place",
                  "User",
                  "Review"]
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    storage = models.storage

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ')

    def do_EOF(self, args):
        """Handle EOF to exit program"""
        return True

    def emptyline(self):
        """Override the cmd with empty line"""
        pass

    def do_quit(self, args):
        """Exit the command"""
        return True

    def help_quit(self):
        """Prints out the help doc for quit"""
        print("Quit command to exit program\n")

    def postcmd(self, stp, ln):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stp

    def do_create(self, args):
        """Create a new instance of model"""
        if not args:
            print("** class name missing **")
        elif args not in self.model_list:
            print("** class doesn't exist **")
        else:
            obj = eval(args)()
            obj.save()
            print(obj.id)

    def help_create(self):
        """Print info for the create method"""
        print("Create a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Shows an individual object"""
        model_id_list = args.split()
        if len(model_id_list) == 0:
            print("** class name missing **")
            return
        else:
            model = model_id_list[0]
            if model not in self.model_list:
                print("** class doesn't exist **")
                return
        if len(model_id_list) == 1:
            print("** instance id missing **")
            return
        else:
            idx = model_id_list[1]
            try:
                print(self.storage.all()[model + "." + idx])
                return
            except KeyError:
                print("** no instance found **")
                return

    def help_show(self):
        """Print out show documentation"""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage.all().items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """Prints Count documentation"""
        print("Usage: count <class_name>")

    def do_destroy(self, args):
        """Destroy an instance based on the class name and id"""
        model_id_list = args.split()
        if len(model_id_list) == 0:
            print("** class name missing **")
            return
        else:
            model = model_id_list[0]
            if model not in self.model_list:
                print("** class doesn't exist **")
                return
        if len(model_id_list) == 1:
            print("** instance id missing **")
            return
        else:
            idx = model_id_list[1]
            try:
                del self.storage.all()[model + "." + idx]
                self.storage.save()
                return
            except KeyError:
                print("** no instance found **")
                return

    def help_destroy(self):
        """Prints the destroy documentation"""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """Prints all string rep of all instances based
        or not on the class name
        """
        if not args:
            # print(srlf.storage.all())
            con_list = []
            for key, obj in self.storage.all().items():
                con_list.append(obj)
            print([str(x) for x in con_list])
        elif args not in self.model_list:
            print("** class doesn't exist **")
        else:
            con_list = []
            for key, obj in self.storage.all().items():
                if obj.__class__.__name__ == args:
                    con_list.append(str(obj))
                print([str(x) for x in con_list])

    def help_all(self):
        """Prints all command documentation"""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        model_id_attr_list = shlex.split(args)
        if len(model_id_attr_list) == 0:
            print("** class name missing **")
            return
        else:
            model = model_id_attr_list[0]
            if model not in self.model_list:
                print("** class doesn't exist **")
                return

        if len(model_id_attr_list) == 1:
            print("** instance id missing **")
            return
        else:
            idx = model_id_attr_list[1]
            try:
                obj = self.storage.all()[model + "." + idx]
            except KeyError:
                print("** no instance found **")
                return

        if len(model_id_attr_list) == 2:
            print("** attribute name missing **")
            return
        else:
            attr = model_id_attr_list[2]

        if len(model_id_attr_list) == 3:
            print("** value missing **")
            return
        else:
            val = model_id_attr_list[3]

        setattr(obj, attr, cast_str_int_float(val))
        obj.save()

    def cast_str_int_float(val):
        """Cast a value to its proper type

        Args:
            val (str): value to cast

        Returns:
            int, float or str: depends of the type of value
        """
        try:
            return int(val)
        except ValueError:
            pass
        try:
            return float(val)
        except ValueError:
            return val

    def help_update(self):
        """print the update documentation"""
        print("Updates an object with new information")
        print("[Usage]: update <className> <id> <attrName> <attVal>\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

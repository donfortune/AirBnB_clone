#!/usr/bin/python3

"""Console Module

This module implements a command-line interface for interacting with an AirBnB clone.
"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class

    Implements a command-line interpreter for the AirBnB clone.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)"""
        print("")  # print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def help_quit(self):
        """Prints help message for the quit command"""
        print("Quit command: Exits the program")

    def help_EOF(self):
        """Prints help message for the EOF command"""
        print("EOF command: Exits the program with Ctrl+D")

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file), and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel"]:  # Add other model classes here
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel"]:  # Add other model classes here
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key in objs:
            del objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:  # Add other model classes here
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in objs.values() if args[0] in str(obj)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel"]:  # Add other model classes here
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objs[key]
        setattr(obj, args[2], args[3])
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()


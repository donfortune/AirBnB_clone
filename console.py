#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.user import User
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
        """Create a new instance of BaseModel"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ['User']:  # Add other class names here if needed
            print("** class doesn't exist **")
            return
        new_user = User()
        new_user.save()
        print(new_user.id)

    def do_show(self, arg):
        """Show instance based on the class name and id"""
        args = arg.split()
        if len(args) < 2:
            print("** mising**" if len(args) == 0 else "** instance **")
            return
        class_name = args[0]
        obj_id = args[1]
        if class_name not in ['User']:  # Add other class names here if needed
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, obj_id)
        instances = storage.all().values()
        class_name = type(obj).__name__
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroy instance based on the class name and id"""
        args = arg.split()
        if len(args) < 2:
            print("** class" if len(args) == 0 else "** id miss **")
            return
        class_name = args[0]
        obj_id = args[1]
        if class_name not in ['User']:  # Add other class names here if needed
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if len(args) == 0:
            instances = storage.all().values()
            print([str(obj) for obj in instances])
        elif args[0] not in ['User']:  # Add other class names here if needed
            print("** class doesn't exist **")
        else:
            instances = storage.all().values()
            class_name = type(obj).__name__
            print([str(obj) for obj in instances if class_name == args[0]])

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 3:
            print(" " if len(args) == 0 else "id" if len(args) == 1 else " ")
            return
        class_name = args[0]
        obj_id = args[1]
        if class_name not in ['User']:  # Add other class names here if needed
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        value = args[3]
        setattr(storage.all()[key], attribute_name, value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

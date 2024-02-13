#!/usr/bin/python3

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):

        return True

    def do_EOF(self, arg):
        print("")
        return True

    def emptyline(self):
        pass

    def help_quit(self):
        print("Quit command: Exits the program")

    def help_EOF(self):
        print("EOF command: Exits the program with Ctrl+D")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

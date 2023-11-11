#!/usr/bin/python3
"""Console module"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB"""

    # Check for interactive/non-interactive mode
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Handle EOF to exit program"""
        return True

    def emptyline(self):
        """Override the cmd with empty line"""
        pass

    def do_quit(self, arg):
        """Exit the command"""
        return True

    def help_quit(self):
        """Prints out the help doc for quit"""
        print("Quit command to exit program\n")



if __name__ == '__main__':
    HBNBCommand().cmdloop()

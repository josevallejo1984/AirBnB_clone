#!/usr/bin/python3
"""New class inherit from cmd"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Consol for safe database."""

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """Signal C+d for exit."""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        sys.exit()

    def emptyline(self):
        """Overwrite method emptyline."""
        print('', end="")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

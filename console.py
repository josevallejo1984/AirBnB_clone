#!/usr/bin/python3
"""New class inherit from cmd"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Consol for safe database."""

    prompt = '(hbnb)'

    def do_create(self, line):
        """Create classes"""
        if self.check_class_name(line):
            try:
                new = eval(line + "()")
                new.save()
                print(new.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Show instances"""
        key = self.found_class_name(line)
        if key is not None:
            all_objs = storage.all()
            try:
                obj = all_objs[key]
                print(obj)
            except Exception:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroy instances"""
        key = self.found_class_name(line)
        if key is not None:
            all_objs = storage.all()
            try:
                all_objs.pop(key)
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, line):
        """Show all instnaces"""
        new_list = []
        all_objs = storage.all()
        if len(line) != 0:
            for key, value in all_objs.items():
                if line == key.split('.')[0]:
                    obj = all_objs[key]
                    new_list.append(obj.__str__())
        else:
            for key, value in all_objs.items():
                obj = all_objs[key]
                new_list.append(obj.__str__())
        print(new_list)

    def do_update(self, line):
        """Update console"""
        key = self.found_class_name(line)
        if key is not None:
            args = line.split(' ')
            if len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                if args[3][0] and args[3][-1] != '"':
                    try:
                        args[3] = int(args[3])
                    except ValueError:
                        try:
                            args[3] = float(args[3])
                        except ValueError:
                            pass

                all_objs = storage.all()
                obj = all_objs[key]
                obj.__dict__.update({args[2]: args[3]})
                obj.save()

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

    def check_class_name(self, name=""):
        """Check if stdin user typed class name and id."""
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Check class id"""
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """Find the name class."""
        if self.check_class_name(name) and self.check_class_id(name):
            args = name.split(' ')
            key = args[0] + '.' + args[1]
            all_objs = storage.all()
            for name_class in all_objs.keys():
                if args[0] == name_class.split('.')[0]:
                    return key
            print("** class doesn't exist **")
        return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
import cmd

class MyCmd(cmd.Cmd):
    """ making use of cmd"""

    prompt = "(hbnb) "
    
    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        print()
        return True

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True
    
    def emptyline(self):
        """Doesn't do anything on Enter
        """
        pass

if __name__ == '__main__':
    MyCmd().cmdloop()

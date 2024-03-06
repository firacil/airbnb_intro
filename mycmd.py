#!/usr/bin/python3
import cmd

class MyCmd(cmd.Cmd):
    """ making use of cmd"""

    prompt = "(hbnb) "

    def do_echo(self, args):
        """ handling the echo command"""
        print(args)

    def do_quit(self, args):
        return True

if __name__ == '__main__':
    MyCmd().cmdloop()

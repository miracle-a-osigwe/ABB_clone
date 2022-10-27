import cmd
import sys

class Cmd(cmd.Cmd):
    intro = "Welcome to the AirBnB-clone shell.   Type help or ? to list commands.\n"
    prompt = "(hbnb) "
    #ruler = "*"
    doc_header = """A help function that provides examples (type help <command>) to see the help function of the command 
    or <type help show> to see all the available commands"""

    def do_help(self, arg):
        """A help method that shows the use cases of the program"""
        print(self.ruler*150)
        print(self.doc_header)
        print(self.ruler*150)

    def do_shell(self, *args):
        """An interactive shell initiator"""
        for arg in args:
            pass

    def do_exit(self, arg):
        """A command that exits the shell environment"""
        print("Thank you for using the shell, cheers...")
        return True

if __name__ == '__main__':
    Cmd().cmdloop()
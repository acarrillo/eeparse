#!/usr/bin/env python


class EEMathParser():
    def __init__(self):
        self.components = dict()

    def parse(self, cmd):
        """
        Parses input from input prompt.
        """
        if cmd == 'exit':
            return True # Tells program to quit
        elif '=' in cmd:
            tokenized_cmd = cmd.split('=')
            self.components[tokenized_cmd[0].strip(' ')] = tokenized_cmd[1].strip(' ')
        elif cmd in self.components.keys():
            print self.components[cmd]
        return False

    def do_loop(self):
        do_quit = False
        while not do_quit:
            cmd = raw_input('>>> ')
            do_quit = self.parse(cmd)

if __name__ == '__main__':
    EEMathParser().do_loop()

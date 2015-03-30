#!/usr/bin/env python


class EEMathParser():
    def __init__(self):
        self.components = dict()

    def parse_value(self, value):
        """
        Parses magnitude from the value. If a user types in "10u", stores this as 10 x 10^-6
        """
        # These are prefixes to be parsed out, like 10u for 10uF
        prefixes = ['P', 'T', 'G', 'M', 'k', 'o', 'm', 'u', 'n', 'p', 'f']
        powers = dict()
        order = 15
        for pf in prefixes:
            powers[pf] = order
            order = order - 3

        quantity = 0
        order = 0
        has_prefix = False
        for pf in prefixes:
            if pf in value:
                quantity = float(value.strip(pf))
                order = powers[pf] # Looks up what power base 10 is raised
                has_prefix = True
                break

        # If no prefix was found, assume base unit 10^0
        if not has_prefix:
            order = 0
            quantity = float(value)

        return (quantity, order)


    def parse_cmd(self, cmd):
        """
        Parses input from input prompt.
        """
        if cmd == 'exit':
            return True # Tells program to quit
        elif '=' in cmd:
            tokenized_cmd = cmd.split('=')
            component_label = tokenized_cmd[0].strip(' ')
            component_value = tokenized_cmd[1].strip(' ')
            self.components[component_label] = self.parse_value(component_value)
        elif cmd in self.components.keys():
            print self.components[cmd]
        return False

    def do_loop(self):
        do_quit = False
        while not do_quit:
            cmd = raw_input('>>> ')
            do_quit = self.parse_cmd(cmd)

if __name__ == '__main__':
    EEMathParser().do_loop()

import os, sys

class artm:

    def __init__(self):
        self.dir = os.path.abspath(os.curdir)
        self.path = self.dir + '\\' + sys.argv[1]

        self.modules = [
            'output', '='
        ]

        self.var = []
        self.vars = {}

        try:
            self.read_file()
            self.compile()
        except FileNotFoundError:
            print('Файл не найден')

    def read_file(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            self.content = file.read()
            for ex in self.content.split():
                self.var.append(ex)

    def compile(self):
        a = -1
        for i in self.var:
            a += 1
            if i == '=':
                if self.var[a-1][0] in [str(i) for i in range(0, 10)]:
                    print(f'Error in name var {self.var[a-1]}')
                    continue

                if self.var[a+1][0] == '"' and self.var[a+1][-1] == '"':
                    self.vars[self.var[a-1]] = [self.var[a+1].replace('"', ''), 'string']

                elif self.var[a+1] in self.vars.keys():
                    self.vars[self.var[a-1]] = self.vars[self.var[a+1]]

                elif self.var[a+1].isdigit():
                    self.vars[self.var[a-1]] = [str(self.var[a+1]), 'integer']

                elif self.var[a+1] not in self.vars.keys():
                    print(f'Name {self.var[a+1]} not defined')

                else:
                    print('Syntax Error in ' + self.var[a+1])

            if i.strip()[:6] == 'output':
                let = i[7:i.find(')')]
                if len(let) == 0:
                    print()
                    continue
                keys = list(self.vars.keys())
                if let in keys:
                    type_ = self.vars[keys[keys.index(let)]][1]
                    if type == 'string':
                        print(str(self.vars[keys[keys.index(let)]][0]))
                    else:
                        print(self.vars[keys[keys.index(let)]][0])

                elif let not in keys:
                    if let.isdigit():
                        print(let)
                    elif let[0] + let[-1] == '""':
                        print(let[1:len(let)-1])
                    elif '"' not in let and "'" not in let:
                        print(f'Name {let} is not defined')
                    else:
                        print(f'Syntax error in {let}')


a = artm()

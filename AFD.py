from PySimpleAutomata import DFA, automata_IO

class Estado:
    def __init__(self):
        print("Hola")

class Transicion:
    c1 = ''
    c2 = ''
    edo = Estado()

    def __init__(self):
        edo = None

    def __init__(self, c, e):
        self.c1 = c
        self.c2 = c
        self.edo = e

    def __init__(self, c1, c2, e):
        self.c1 = c1
        self.c2 = c2
        self.edo = e

    def setter(self, c, e):
        self.c1 = c
        self.c2 = c
        self.edo = e

    def setter(self,c1, c2, e):
        self.c1 = c1
        self.c2 = c2
        self.edo = e

    def getter(self):
        return c1,c2,edo



def main():
    dfa_example = automata_IO.dfa_dot_importer('afd.dot')
    #DFA.dfa_completion(dfa_example)
    #new_dfa=DFA.dfa_minimization(dfa_example)

    automata_IO.dfa_to_dot(dfa_example, 'hola', '.')

if __name__ == "__main__":
    main()        
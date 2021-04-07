from Estado import *

class Trans():
    def __init__(self, edoi, edof, rango):
        self.EI = edoi
        self.EF = edof
        self.S = rango

    def __str__(self):
        return "s%s -> s%s [label=\"%s\"]"%(self.EI.getNombre(), self.EF.getNombre(),self.S)
    
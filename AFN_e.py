from PySimpleAutomata import DFA,automata_IO
from Estado import *
from Transicion import *

class AFN_e():
    def __init__(self, numAFN, K = list(), Sigma = list(), S = list(), Z = list(), M = list()):
        self.K = K
        self.Sigma = Sigma
        self.S = S
        self.Z = Z
        self.M = M
        self.N = numAFN
    
    def nuevoAFNSimple(self,token = -1):
        """Crea un AFN de una transicion y dos estados"""
        vi = input("Ingresa el caracter inicial: ")
        vf = input("Ingresa el caracter final: ")

        A = self.creaEdo(True, -1)
        B = self.creaEdo(False, token)
        t = self.creaTrans(A,B,vi,vf)

        self.actAlfabeto(vi,vf)

        return self

    
    def unir(self, token):
        e = [self.creaEdo(True, -1), 
            self.creaEdo(False,-1), 
            self.creaEdo(False, -1), 
            self.creaEdo(False, token)]
        t = [self.creaTrans(e[0],e[1],"£","£"),
            self.creaTrans(e[1],)
        ]




    def creaEdo(self, raiz, token):
        """Crea un estado y lo agrega al AFN"""
        e = Estado(str(len(self.K)),raiz, token)
        self.K.append(e)
        if e.Raiz:
            self.S = e
        if e.Token>-1:
            self.Z = e
        return e
        
        

    def creaTrans(self,edoi, edof, vi, vf):
        """Crea una transicion y se agrega al AFN"""
        if vi == vf:
            t = Trans(edoi,edof,str(vi))
        else:
            t = Trans(edoi,edof,"%c-%c"%(vi,vf))
        
        self.M.append(t)

    def actAlfabeto(self, vi, vf):
        """Funcion para actualizar el alfabeto"""
        VI, VF = ord(vi), ord(vf)
        rango = VF - VI + 1
        for i in range(rango):
            self.Sigma.append(chr(VI))

    def getEI(self):
        return self.S
    
    def getEF(self):
        return self.Z

#------------------------MOSTRAR-------------------
    def mostrar(self):
        f = open("Token" + str(self.N) + ".dot", "w")
        f.write("digraph{\nfake [style=invisible]\nfake -> s0 [style=bold]\n\n")


        print("Alfabeto que acepta el automata")
        print(self.Sigma)

        print("Estado de inicio del automata")
        for e in self.S:
            print(self.S.__str__())

        print("Conjunto de Estados(Objeto) no vacios")
        for e in self.K:
            print(e.__str__())
            f.write(e.__str__())
            f.write("\n")
        f.write("\n")

        print("Conjunto de Estados(Objeto) de aceptacion")
        for e in self.Z:
            print(self.Z.__str__())

        print("Conjunto de Transiciones(Objeto)")
        for e in self.M:
            print(e.__str__())
            f.write(e.__str__()+"\n")

        f.write("\n}")
        f.close()

        afn = automata_IO.nfa_dot_importer("Token" + str(self.N) + ".dot")
        automata_IO.nfa_to_dot(afn, "Token" + str(self.N), ".")

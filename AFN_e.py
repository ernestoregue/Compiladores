from PySimpleAutomata import DFA,automata_IO
from Estado import *
from Transicion import *

class AFN_e():
    def __init__(self, numAFN, K = list(), Sigma = list(), S = object(), Z = object(), M = list()):
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

    @staticmethod
    def unir(AFNS, token):
        RAFN = AFN_e(4)
        e = []

        for i in range(len(AFNS)):
            for j in range(len(AFNS[i].K)):
                RAFN.K.append(AFNS[i].K[j])
                RAFN.M.append(AFNS[i].M[j])
                RAFN.Sigma.append(AFNS[i].Sigma[j])


        for i in range(4):
            if i == 0:
                e.append(RAFN.creaEdo(True,-1))
                RAFN.S = e[i]
            elif i == 3:
                e.append(RAFN.creaEdo(False, token))
                RAFN.Z = e[i]
            else:
                e.append(RAFN.creaEdo(False,-1))
                

        RAFN.creaTrans(e[0], e[1], "£", "£")
        RAFN.creaTrans(e[1], AFNS[0].S, "£", "£")
        RAFN.creaTrans(e[1], AFNS[1].S, "£", "£")
        RAFN.creaTrans(e[1], AFNS[1].S, "£", "£")
        RAFN.creaTrans(AFNS[0].Z, e[2], "£", "£")
        RAFN.creaTrans(AFNS[1].Z, e[2], "£", "£")
        RAFN.creaTrans(e[2], e[3], "£", "£")
        
        for i in range(len(AFNS)):
            AFNS[i].S.setEdoI(False)
            AFNS[i].Z.setToken(-1)

        return RAFN

    @staticmethod
    def concat(AFNS, token):
        RAFN = AFN_e(5)

        for i in range(len(AFNS)):
            for j in range(len(AFNS[i].K)):
                RAFN.K.append(AFNS[i].K[j])
                RAFN.M.append(AFNS[i].M[j])
                RAFN.Sigma.append(AFNS[i].Sigma[j])

        
        AFNS[0].S.setEdoI(False)
        RAFN.S = AFNS[0].S
        RAFN.S.setEdoI(True)

        AFNS[1].Z.setToken(-1)
        RAFN.Z = AFNS[1].Z
        RAFN.Z.setToken(token)
        
        AFNS[1].S.setEdoI(False)
        AFNS[0].Z.setToken(-1)
        AFNS[0].Z = AFNS[1].S


        

        return RAFN



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
        print(self.S.__str__())

        print("Conjunto de Estados(Objeto) no vacios")
        for e in self.K:
            print(e.__str__())
            f.write(e.__str__())
            f.write("\n")
        f.write("\n")

        print("Conjunto de Estados(Objeto) de aceptacion")
        print(self.Z.__str__())

        print("Conjunto de Transiciones(Objeto)")
        for e in self.M:
            print(e.__str__())
            f.write(e.__str__()+"\n")

        f.write("\n}")
        f.close()

        afn = automata_IO.nfa_dot_importer("Token" + str(self.N) + ".dot")
        automata_IO.nfa_to_dot(afn, "Token" + str(self.N), ".")

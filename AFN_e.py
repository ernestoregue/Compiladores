from PySimpleAutomata import NFA,automata_IO
from Estado import *
from Transicion import *

class AFN_e():
    def __init__(self, numAFN, K = list(), Sigma = list(), S = object(), Z = object(), M = list()):
        """Constructor del AFN"""
        self.K = K
        self.Sigma = Sigma
        self.S = S
        self.Z = Z
        self.M = M
        self.N = numAFN
    
    def nuevoAFNSimple(self,token = -1):
        """Crea un AFN de una transicion y dos estados, incluyendo su token"""
        vi = input("Ingresa el caracter inicial: ")
        vf = input("Ingresa el caracter final: ")

        A = self.creaEdo(True, -1)
        B = self.creaEdo(False, token)
        t = self.creaTrans(A,B,vi,vf)

        self.actAlfabeto(vi,vf)

        return self

    @staticmethod
    def unir(AFNS, token, numAFN):
        """Toma una lista de AFNS y los une con la forma de Thompson\n Se hace un nuevo token y un numero de AFN"""
        """AFN_e.unir([AFN1,AFN2,AFN3,...], token, numAFN)"""
        RAFN = AFN_e(numAFN)
        
        e1 = RAFN.creaEdo(True, -1)
        e2 = RAFN.creaEdo(False, -1)
        e3 = RAFN.creaEdo(False, -1)
        e4 = RAFN.creaEdo(False, token)

        RAFN.creaTrans(e1,e2, "£", "£")
        RAFN.creaTrans(e3,e4, "£", "£")

        for i in range(len(AFNS)):
            RAFN.creaTrans(e2,AFNS[i].S, "£", "£")
            RAFN.creaTrans(AFNS[i].Z, e3, "£", "£")
        
        for i in range(len(AFNS)):
            AFNS[i].S.setEdoI(False)
            AFNS[i].Z.setToken(-1)
            RAFN.K += AFNS[i].K
            RAFN.M += AFNS[i].M
            RAFN.Sigma += AFNS[i].Sigma

        RAFN.S = e1
        RAFN.Z = e4

        return RAFN

    @staticmethod
    def concat(AFNS, token, numAFN):
        """Método para concatenar DOS AFNS"""
        """AFN_e.concat([AFN1,AFN2], token, numAFN)"""
        RAFN = AFN_e(numAFN)

        A = AFNS[0].S
        B = AFNS[1].S.getNombre()
        C = AFNS[1].Z
        D = AFNS[0].Z.getNombre()
        


        for i in range(len(RAFN.M)):
            if RAFN.M[i].EF.getNombre() == D:
                RAFN.M[i].EF.setNombre(B)

        for i in range(len(AFNS)):
            AFNS[i].S.setEdoI(False)
            AFNS[i].Z.setToken(-1)

        RAFN.S = A
        A.setEdoI(True)
        RAFN.Z = C
        C.setToken(token)

        return RAFN

    @staticmethod
    def cpositiva(AFN, token):
        """Reforma el AFN para ponerle una cerradura positiva"""

        AFN.creaTrans(AFN.Z,AFN.S, "£", "£")
        
        A = AFN.S
        B = AFN.Z

        e1 = AFN.creaEdo(True, -1)
        e2 = AFN.creaEdo(False, token)
        
        AFN.creaTrans(e1,A, "£", "£")
        A.setEdoI(False)
        AFN.S = e1

        AFN.creaTrans(B, e2, "£", "£")
        B.setToken(-1)
        AFN.Z = e2

        return AFN

    @staticmethod
    def ckleen(AFN, token):
        """Reforma el AFN para ponerle una cerradura de Kleen"""
        RFNA = AFN_e.cpositiva(AFN,token)
        
        RFNA.creaTrans(RFNA.S,RFNA.Z, "£", "£")

        return RFNA

    @staticmethod
    def copcional(AFN, token):
        """Reforma el AFN para ponerle una cerradura opcional"""
        
        A = AFN.S
        B = AFN.Z

        e1 = AFN.creaEdo(True, -1)
        e2 = AFN.creaEdo(False, token)
        
        AFN.creaTrans(e1,A, "£", "£")
        A.setEdoI(False)
        AFN.S = e1

        AFN.creaTrans(B, e2, "£", "£")
        B.setToken(-1)
        AFN.Z = e2

        AFN.creaTrans(e1,e2, "£", "£")

        return AFN

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

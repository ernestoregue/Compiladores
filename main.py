from AFN_e import *
from PySimpleAutomata import NFA,automata_IO

def main():
    ArregloAFNS = []
    
    AFN1 = AFN_e(len(ArregloAFNS))
    AFN1.nuevoAFNSimple(10)
    AFN1 = AFN_e.cpositiva(AFN1, 10)
    ArregloAFNS.append(AFN1)
    AFN1.mostrar()

    AFN2 = AFN_e(len(ArregloAFNS))
    AFN2.nuevoAFNSimple(20)
    AFN2 = AFN_e.ckleen(AFN2, 20)
    ArregloAFNS.append(AFN2)
    AFN2.mostrar()

    AFN3 = AFN_e(len(ArregloAFNS))
    AFN3.nuevoAFNSimple(30)
    AFN3 = AFN_e.copcional(AFN3, 30)
    ArregloAFNS.append(AFN3)
    AFN3.mostrar()

    AFN4 = AFN_e(len(ArregloAFNS))
    AFN4.nuevoAFNSimple(30)
    #AFN3 = AFN_e.cpositiva(AFN3, 30)
    ArregloAFNS.append(AFN4)
    AFN4.mostrar()

    RAFN = AFN_e.unir([AFN1,AFN2,AFN3],40,(AFN1.N+AFN2.N))
    RAFN.mostrar()
    RAFN2 = AFN_e.concat([RAFN,AFN4],70, len(ArregloAFNS) + 10)
    RAFN2.mostrar()

if __name__ == "__main__":
    main()
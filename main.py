from AFN_e import *
from PySimpleAutomata import NFA,automata_IO

def main():

    AFN1 = AFN_e(1)
    AFN1.nuevoAFNSimple(10)
    AFN1 = AFN_e.cpositiva(AFN1, 10)
    AFN1.mostrar()

    AFN2 = AFN_e(2)
    AFN2.nuevoAFNSimple(20)
    AFN2 = AFN_e.ckleen(AFN2, 20)
    AFN2.mostrar()

    AFN3 = AFN_e(3)
    AFN3.nuevoAFNSimple(30)
    AFN3 = AFN_e.copcional(AFN3,30)
    AFN3.mostrar()

    RAFN = AFN_e.unir([AFN1,AFN2],40)
    RAFN2 = AFN_e.concat([RAFN,AFN3],50)
    RAFN2.mostrar()

if __name__ == "__main__":
    main()
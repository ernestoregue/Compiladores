import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import pylab

class AFN_e:
    G=nx.MultiDiGraph()
    #creacion de un nodo basico
    def __init__(self,EdoInicial,EdoFinal,Simbolo):
        self.G.add_node(EdoInicial)
        self.G.add_node(EdoFinal)
        self.G.add_edge(EdoInicial,EdoFinal,Simbolo)
    
    def unirCon(self):
        pass

    def concatCon(self):
        pass

    def cerraduraPositiva(self):
        pass

    def opcion(self):
        pass

    def cerraduraKleene(self):
        pass
    
    def getTransicion(self):
        pass

    def getEdoInicial(self):
        pass

    def getEdoFinal(self):
        pass

    def setEdoInicial(self):
        pass

    def setEdoFinal(self):
        pass

    def setetTransicion(self):
        pass

    def mostrarAutomata(self):
        #
        pos = nx.circular_layout(self.G)
        #pos = nx.spring_layout(self.G)
        nx.draw(self.G,pos,with_labels = True )  
        plt.show() 
        print(self.G.graph)
        print(self.G.nodes)
        print(self.G.nodes(data = True))
        print(self.G.nodes(data = 'type'))
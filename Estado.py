class Estado():

    #Constructor
    def __init__(self, nombre, raiz = False, token = -1):
        """Crea un estado"""
        self.Nombre = nombre
        self.Token = token
        self.Raiz = raiz
    
    #Set/Get Edo. inicial
    def setEdoI(self, raiz):
        """Cambia entre estado raiz o no"""
        self.Raiz = raiz
    def isEdoI(self):
        """Retorna si es raiz o no"""
        return self.Raiz

    #Set/Get Token de estado
    def setToken(self, token):
        """Cambia el token"""
        self.Token = token
    def getToken(self):
        """Obtiene el token"""
        return self.Token

    #Set/Get Nombre de estado
    def getNombre(self):
        """Retorna el nombre del estado"""
        return self.Nombre
    def setNombre(self, nombre):
        """Cambia el nombre del estado"""
        self.Nombre = nombre

    def __str__(self):
        """Retorna un string para imprimir los estados\nFormato : sn [root,shape]"""
        if self.Token > -1:
            return "s%s [shape=doublecircle]" %(self.Nombre)
        elif self.Raiz == True:
            return "s%s [root=true]"%(self.Nombre)
        else:
            return "s%s"%(self.Nombre)
    
    
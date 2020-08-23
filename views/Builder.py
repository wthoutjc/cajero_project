from abc import ABC, abstractmethod

from views.FactoriaInterfaz import *

class AbstractBuilder(ABC):

    @abstractmethod
    def __init__(self):
        self.AbstractInterfaz = None
    
    @abstractmethod
    def buildPantalla(self):
        pass

class BuilderPantalla0(AbstractBuilder):

    def __init__(self):
        self.AbstractInterfaz = FabricaScreenPrincipal()
    
    def buildPantalla(self):
        return self.AbstractInterfaz.crearPantalla()

class BuilderPantalla1(AbstractBuilder):

    def __init__(self):
        self.AbstractInterfaz = FabricaScreens()
    
    def buildPantalla(self):
        return self.AbstractInterfaz.crearPantalla()

class BuilderPantalla2(AbstractBuilder):

    def __init__(self):
        self.AbstractInterfaz = FabricaScreens2()
    
    def buildPantalla(self):
        return self.AbstractInterfaz.crearPantalla()

class BuilderAgrario(AbstractBuilder):

    def __init__(self):
        self.AbstractInterfaz = FabricaAgrario()
    
    def buildPantalla(self):
        return self.AbstractInterfaz.crearPantalla()

class BuilderBancolombia(AbstractBuilder):

    def __init__(self):
        self.AbstractInterfaz = FabricaBancolombia()
    
    def buildPantalla(self):
        return self.AbstractInterfaz.crearPantalla()

class BuilderDavivienda(AbstractBuilder):

    def __init__(self):
        self.AbstractInterfaz = FabricaDavivienda()
    
    def buildPantalla(self):
        return self.AbstractInterfaz.crearPantalla()

class BuilderManager():

    def __init__(self):
        self.builder = None
    
    def setBuilder(self, builder):
        self.builder = builder
    
    def buildCajero(self):
        return self.builder.buildPantalla()
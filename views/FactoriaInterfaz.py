from abc import ABC, abstractmethod

from views.ProductoInterfaz import *

class AbstractInterfaz(ABC):
    
    @abstractmethod
    def crearPantalla(self):
        pass

class FabricaScreenPrincipal(AbstractInterfaz):

    def crearPantalla(self):
        return Pantalla0().getImage()

class FabricaScreens(AbstractInterfaz):

    def crearPantalla(self):
        return Pantalla1().getImage()

class FabricaScreens2(AbstractInterfaz):

    def crearPantalla(self):
        return Pantalla2().getImage()


class FabricaAgrario(AbstractInterfaz):

    def crearPantalla(self):
        return PantallaAgrario().getImage()


class FabricaBancolombia(AbstractInterfaz):

    def crearPantalla(self):
        return PantallaBancolombia().getImage()
        

class FabricaDavivienda(AbstractInterfaz):

    def crearPantalla(self):
        return PantallaDavivienda().getImage()
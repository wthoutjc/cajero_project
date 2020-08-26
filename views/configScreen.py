from views.Builder import *

class configScreen():

    def setScreen(self, posicion):
        self.ii2 = Image.open(self.getBuilders(posicion))
        self.ii2.thumbnail((465,365))
        self.ii2 = ImageTk.PhotoImage(self.ii2)
        return self.ii2

    def getBuilders(self, posicion):
        self.app = BuilderManager()
        self.opciones = [BuilderPantalla0(), BuilderPantalla1(),BuilderPantalla2(), BuilderAgrario(), BuilderBancolombia(), BuilderDavivienda()]
        self.app.setBuilder(self.opciones[posicion])
        return self.app.buildCajero()

    
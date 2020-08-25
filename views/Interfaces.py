import tkinter as tk
from tkinter import ttk
from tkinter import *

from PIL import Image, ImageTk

from views.configScreen import configScreen
from views.Estado import Estado

class Interfaces():

    def __init__(self, root):

        self.root = root
        self.config = configScreen()
        self.status = Estado()
        self.status.setEstado(0)

    def screen0(self):

        self.status.setEstado(0)

        self.fondo = Label(self.root,image=self.config.setScreen(0), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Registrarse" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Iniciar Sesión" )
        self.text2.place(x=423, y = 360)     

    def screen1Register(self):

        self.status.setEstado(11)

        self.fondo = Label(self.root,image=self.config.setScreen(1), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Volver" )
        self.text2.place(x=423, y = 360)

        self.lblName =tk.Label(self.root,text= "Nombre").place(x=190, y=150)
        self.nombreUsu = tk.StringVar()
        self.txtName = ttk.Entry(self.root,textvariable=self.nombreUsu).place(x=250, y=150)
        self.lblApellido =tk.Label(self.root,text= "Apellido").place(x=190, y=190)
        self.apellidoUsu = tk.StringVar()
        self.txtApellido = ttk.Entry(self.root,textvariable=self.apellidoUsu).place(x=250, y=190)
        self.lblIdPersona =tk.Label(self.root,text="Cedula").place(x=190, y=230)
        self.idPersona = tk.StringVar()
        self.txtIdPersona = ttk.Entry(self.root,textvariable=self.idPersona).place(x=250, y=230)
        self.lblBanco =tk.Label(self.root,text= "Banco").place(x=390, y=150)
        self.comboboxbanco = ttk.Combobox(self.root, state = "readonly" )
        self.comboboxbanco.place(x=440, y=150)
        self.comboboxbanco["values"] = ["Agrario", "Bancolombia", "Davivienda"]
        self.lblSaldo =tk.Label(self.root,text= "Saldo Inicial").place(x=175, y=270)
        self.saldo = tk.StringVar()
        self.txtsaldo = ttk.Entry(self.root,textvariable=self.saldo).place(x=250, y=270)
        self.lblPassword =tk.Label(self.root,text= "Password").place(x=190, y=300)
        self.password = tk.StringVar()
        self.txtclave = ttk.Entry(self.root,textvariable=self.password).place(x=250, y=300)
    
    def getNombre(self):
        return self.nombreUsu.get()
    
    def getApellido(self):
        return self.apellidoUsu.get()
    
    def getIdPersona(self):
        return self.idPersona.get()
    
    def getBanco(self):
        return self.comboboxbanco.get()

    def getSaldo(self):
        return self.saldo.get()

    def getPassword(self):
        return self.password.get()

    def screen1LogIn(self):

        self.status.setEstado(12)

        self.fondo = Label(self.root,image=self.config.setScreen(1), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Volver" )
        self.text2.place(x=423, y = 360)

        self.lblIdPersona2 =tk.Label(self.root,text= "Cédula").place(x=200, y=230)
        self.idPersona2 = tk.StringVar()
        self.txtIdPersona2 = ttk.Entry(self.root,textvariable=self.idPersona2).place(x=270, y=230)
        self.lblPassword2 =tk.Label(self.root,text= "Password").place(x=200, y=300)
        self.password2 = tk.StringVar()
        self.txtPassword2 = ttk.Entry(self.root,textvariable=self.password2).place(x=270, y=300)

    def getIdPersona2(self):
        return self.idPersona2.get()
    
    def getPassword2(self):
        return self.password2.get()

    def screenConfirmacion21(self):

        self.status.setEstado(21)

        self.fondo = Label(self.root,image=self.config.setScreen(2), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)
        self.lblSuccess =tk.Label(self.root,text= "Datos confirmados").place(x=230, y=230)

    def screenError22(self):

        self.status.setEstado(22)

        self.fondo = Label(self.root,image=self.config.setScreen(2), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)
        self.lblSuccess =tk.Label(self.root,text= "Datos incorrectos").place(x=330, y=300)
    
    def seteoScreens(self, x):

        self.x = x

        self.fondo = Label(self.root,image=self.config.setScreen(x), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Consignar " )
        self.text1.place(x=450, y = 455)
        self.text2 = Label(self.root, text = "Consultar Saldo" )
        self.text2.place(x=423, y = 360)
        self.text3 = Label(self.root, text = "Retirar Dinero" )
        self.text3.place(x=250, y = 455)
        self.text4 = Label(self.root, text = "Cambio de Clave" )
        self.text4.place(x=250, y = 360)
        self.text5 = Label(self.root, text = "Salir" )
        self.text5.place(x=460, y = 290)

    def screenAgrario(self):
        self.seteoScreens(3)
        self.status.setEstado(3) # Estado 3 = Agrario 3,4,5 -> BANCOS
    
    def screenBancolombia(self):

        self.seteoScreens(4)
        self.status.setEstado(3)

    
    def screenDavivienda(self):

        self.seteoScreens(5)
        self.status.setEstado(3)
    
    def screenConsultarSaldo31(self, saldo):

        self.saldo = saldo

        self.status.setEstado(31)

        self.fondo = Label(self.root,image=self.config.setScreen(2), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.r = Text(self.root, width= 100, height = 75)
        self.r.insert(INSERT, 'Su saldo es: ' + str(self.saldo))
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)

    def getEstado(self):
        return self.status.getEstado()
###############################################
# consultar saldo
    def screenSaldo42(self,nombre,saldo):

        self.nombre = nombre
        self.saldo = saldo

        self.status.setEstado(42)

        self.fondo = Label(self.root,image=self.config.setScreen(2), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)
        self.lblSaldo =tk.Label(self.root,text= "Consulta tu saldo, " + str(self.nombre)).place(x=330, y=300)
        self.lblSaldo =tk.Label(self.root,text= "Tu saldo es: " + str(self.saldo)).place(x=330, y=340)
        #cambio clave

    def screenClave43(self):

        self.status.setEstado(43)

        self.fondo = Label(self.root,image=self.config.setScreen(1), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Volver" )
        self.text2.place(x=423, y = 360)

        self.lablClaveActual = tk.Label(self.root, text = "Clave Actual: " ).place(x=240, y=200)
        self.oldpassword = tk.StringVar()
        self.txtPassword2 = ttk.Entry(self.root,textvariable=self.oldpassword).place(x=360, y=200)
        self.lblIdPersona2 =tk.Label(self.root,text= "Clave Nueva: ").place(x=240, y=250)
        self.newpassword = tk.StringVar()
        self.txtIdPersona2 = ttk.Entry(self.root,textvariable=self.newpassword).place(x=360, y=250)
    
    def getOldPassword(self):
        return self.oldpassword.get()

    def getNewPassword(self):
        return self.newpassword.get()
    
    # Retirar
    def screenRetirar(self):

        self.status.setEstado(44)

        self.fondo = Label(self.root,image=self.config.setScreen(1), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Volver" )
        self.text2.place(x=423, y = 360)

        self.lablConsignar = tk.Label(self.root, text = "Valor a retirar: " ).place(x=240, y=250)
        self.valorR = tk.StringVar()
        self.txtPassword2 = ttk.Entry(self.root,textvariable=self.valorR).place(x=360, y=250)

    def getValorR(self):
        return self.valorR.get()
        
    # Consignar Dinero  
    def screenConsignar(self):

        self.status.setEstado(45)

        self.fondo = Label(self.root,image=self.config.setScreen(1), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Volver" )
        self.text2.place(x=423, y = 360)

        self.lablClaveActual = tk.Label(self.root, text = "idCuenta: " ).place(x=240, y=200)
        self.idCuentaC = tk.StringVar()
        self.txtPassword2 = ttk.Entry(self.root,textvariable=self.idCuentaC).place(x=360, y=200)
        self.lablConsignar = tk.Label(self.root, text = "Valor a Consignar: " ).place(x=240, y=250)
        self.valorC = tk.StringVar()
        self.txtPassword2 = ttk.Entry(self.root,textvariable=self.valorC).place(x=360, y=250)

    def getIdCuentaC(self):
        return self.idCuentaC.get()

    def getValorC(self):
        return self.valorC.get()
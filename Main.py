from tkinter import ttk, messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pyodbc

def VGanado():
    global fondo
    #####################
    fondo = tk.Frame(VPrincipal, bg='light grey')
    fondo.place(relheight=1, relwidth=1)
    ##########################################
    FrameHead = tk.Frame(fondo, bg='green3')
    FrameHead.place(x=0, y=0, relwidth=1, height=60)
    FPL = tk.Label(FrameHead, text='Ganado de  la Granja Ucundinamarca', font=('Great Vibes', 25), bg='green3', fg='white')
    FPL.place(x=20, y=20)
    ######################
    Banner = Image.open('imagenes/banner_ganado.png')
    Banner = Banner.resize((1400,500))
    Banner = ImageTk.PhotoImage(Banner)
    FrameRe = tk.Frame(fondo)
    FrameRe.place(y=60,height=300,relwidth=1)
    FrameReL = tk.Label(FrameRe, image=Banner)
    FrameReL.place(relheight=1,relwidth=1)
    ######################
    FrameEs = tk.Frame(fondo,bg='light grey')
    FrameEs.place(relwidth=1,height=500,y=360)

    Vaca = Image.open('imagenes/vaca.png')
    Vaca = Vaca.resize((100,100))
    Vaca = ImageTk.PhotoImage(Vaca)
    Esp1L = tk.Frame(FrameEs,bg='azure')
    Esp1L.place(x=20,y=20,relwidth=.45,height=100)
    EsvL = tk.Label(Esp1L,text='Bovinos', font=('Great Vibes', 40),bg='azure')
    EsvL.place(relx=.3,y=20)
    Esv = tk.Label(Esp1L, image=Vaca,bg='azure')
    Esv.place(relx=.85,y=0,relheight=1,width=100)
    Esp1L.bind("<Button-1>", VGV)
    EsvL.bind("<Button-1>", VGV)
    Esv.bind("<Button-1>", VGV)

    Cerdo = Image.open('imagenes/cerdo.png')
    Cerdo = Cerdo.resize((100,100))
    Cerdo = ImageTk.PhotoImage(Cerdo)
    Esp2L = tk.Frame(FrameEs,bg='azure')
    Esp2L.place(x=20,y=200,relwidth=.45,height=100)
    EscL = tk.Label(Esp2L,text='Porcinos', font=('Great Vibes', 40),bg='azure')
    EscL.place(relx=.3,y=20)
    Esc = tk.Label(Esp2L, image=Cerdo,bg='azure')
    Esc.place(relx=.85,y=0,relheight=1,width=100)
    Esp2L.bind("<Button-1>", VGC)
    EscL.bind("<Button-1>", VGC)
    Esc.bind("<Button-1>", VGC)
    
    Cabra = Image.open('imagenes/cabra.png')
    Cabra = Cabra.resize((50,100))
    Cabra = ImageTk.PhotoImage(Cabra)
    Esp3L = tk.Frame(FrameEs,bg='azure')
    Esp3L.place(relx=.5,y=200,relwidth=.45,height=100)
    EscaL = tk.Label(Esp3L,text='Caprinos', font=('Great Vibes', 40),bg='azure')
    EscaL.place(relx=.3,y=20)
    Esca = tk.Label(Esp3L, image=Cabra,bg='azure')
    Esca.place(relx=.85,y=0,relheight=1,width=100)
    Esp3L.bind("<Button-1>", VGCa)
    EscaL.bind("<Button-1>", VGCa)
    Esca.bind("<Button-1>", VGCa)

    Gall = Image.open('imagenes/gallina.png')
    Gall = Gall.resize((100,100))
    Gall = ImageTk.PhotoImage(Gall)
    Esp5L = tk.Frame(FrameEs,bg='azure')
    Esp5L.place(relx=.5,y=20,relwidth=.45,height=100)
    EsgL = tk.Label(Esp5L,text='Avicultura', font=('Great Vibes', 40),bg='azure')
    EsgL.place(relx=.3,y=20)
    Esg = tk.Label(Esp5L, image=Gall,bg='azure')
    Esg.place(relx=.85,y=0,relheight=1,width=100)
    Esp5L.bind("<Button-1>", VGG)
    EsgL.bind("<Button-1>", VGG)
    Esg.bind("<Button-1>", VGG)

    B_Atraz = tk.Button(fondo, text='Atraz',bg='green3',command=AtrasG)
    B_Atraz.place(y=680,x=30,width=50,height=25)

    VPrincipal.mainloop()
##############################
def VGV(event):
    global FondoV
    fondo.destroy()
    ###############
    FondoV = tk.Frame(VPrincipal)
    FondoV.place(relheight=1,relwidth=1)
    ###################################
    FrameAn = tk.Frame(FondoV,bg='green3')
    FrameAn.place(relwidth=1,height=200)

    LRaza = tk.Label(FrameAn,text='Raza:',bg='green3',font=('Great Vibes', 25))
    LRaza.place(relx=.1,rely=.3)
    CoRaza = ttk.Combobox(FrameAn, values=['Holstein','Gyr','Jersey','Normando','Pardo suizo'],font=('Great Vibes', 25))
    CoRaza.place(relx=.1,rely=.5,width=200)

    LEdad = tk.Label(FrameAn, text='Edad:(meses)', bg='green3',font=('Great Vibes', 25))
    LEdad.place(relx=.3,rely=.3)
    InEdad = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InEdad.place(relx=.3,rely=.5,width=100)

    LPeso = tk.Label(FrameAn, text='Peso:(Kilos)', bg='green3',font=('Great Vibes', 25))
    LPeso.place(relx=.5,rely=.3)
    InPeso = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InPeso.place(relx=.5,rely=.5,width=100)

    LNum = tk.Label(FrameAn, text='Numero Oreja:', bg='green3',font=('Great Vibes', 25))
    LNum.place(relx=.7,rely=.3)
    InNum = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InNum.place(relx=.7,rely=.5,width=200)
    
    BtnA = tk.Button(FrameAn, text='Agregar',font=('Great Vibes', 15),bg='azure')
    BtnA.place(relx=.87,rely=.15,)
    BtnM = tk.Button(FrameAn, text='Modificar',font=('Great Vibes', 15),bg='azure')
    BtnM.place(relx=.87,rely=.4,)
    BtnE = tk.Button(FrameAn, text='Eliminar',font=('Great Vibes', 15),bg='azure')
    BtnE.place(relx=.87,rely=.7)
    BtnAt = tk.Button(FrameAn,text='Atras',font=('Great Vibes', 15),bg='azure',command=AtrasV)
    BtnAt.place(relx=.01,rely=.1)
    ###################################
    FrameRaza = tk.Frame(FondoV,bg='light gray')
    FrameRaza.place(relwidth=.5,height=545,y=200)

    F1 = tk.Button(FrameRaza,text='Holstein',bg='azure',font=('Great Vibes', 15))
    F1.place(rely=.03,x=50,relwidth=.8,height=80)

    F2 = tk.Button(FrameRaza,text='Gyr',font=('Great Vibes', 15),bg='azure')
    F2.place(rely=.23,x=50,relwidth=.8,height=80)

    F3 = tk.Button(FrameRaza,text='Jersey',font=('Great Vibes', 15),bg='azure')
    F3.place(rely=.43,x=50,relwidth=.8,height=80)

    F4 = tk.Button(FrameRaza,text='Normando',font=('Great Vibes', 15),bg='azure')
    F4.place(rely=.63,x=50,relwidth=.8,height=80)

    F5 = tk.Button(FrameRaza,text='Pardo suizo',font=('Great Vibes', 15),bg='azure')
    F5.place(rely=.83,x=50,relwidth=.8,height=80)
    #####################
    FrameG = tk.Frame(FondoV,bg='azure')
    FrameG.place(relwidth=.5,relheight=1,y=200,relx=.5)
    GridV = ttk.Treeview(FrameG, columns=("Raza","Edad","Peso","Numero oreja","Produccion"))
    GridV.column("#0", width=10)
    GridV.column("Raza", width=200)
    GridV.column("Edad",width=50)
    GridV.column("Peso",width=50)
    GridV.column("Numero oreja",width=100)
    GridV.heading("Raza", text='Raza')
    GridV.heading("Edad", text='Edad\n(meses)')
    GridV.heading("Peso", text="Peso\n(kilos)")
    GridV.heading("Numero oreja", text='Numero oreja')
    GridV.heading("Produccion", text='Produccion\n(Diaria)')
    GridV.place(x=0,y=0,relheight=1,width=680)
    #####################
    VPrincipal.mainloop()
##############################
def VGC(event):
    global FondoC
    fondo.destroy()
    ###############
    FondoC = tk.Frame(VPrincipal)
    FondoC.place(relheight=1,relwidth=1)
    ###################################
    FrameAn = tk.Frame(FondoC,bg='green3')
    FrameAn.place(relwidth=1,height=200)

    LRaza = tk.Label(FrameAn,text='Raza:',bg='green3',font=('Great Vibes', 25))
    LRaza.place(relx=.1,rely=.3)
    CoRaza = ttk.Combobox(FrameAn, values=['San Pedreño','Zungo','Casco de Mula'],font=('Great Vibes', 25))
    CoRaza.place(relx=.1,rely=.5,width=200)

    LEdad = tk.Label(FrameAn, text='Edad:(meses)', bg='green3',font=('Great Vibes', 25))
    LEdad.place(relx=.3,rely=.3)
    InEdad = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InEdad.place(relx=.3,rely=.5,width=100)

    LPeso = tk.Label(FrameAn, text='Peso:(Kilos)', bg='green3',font=('Great Vibes', 25))
    LPeso.place(relx=.5,rely=.3)
    InPeso = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InPeso.place(relx=.5,rely=.5,width=100)

    LNum = tk.Label(FrameAn, text='Numero Oreja:', bg='green3',font=('Great Vibes', 25))
    LNum.place(relx=.7,rely=.3)
    InNum = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InNum.place(relx=.7,rely=.5,width=200)
    
    BtnA = tk.Button(FrameAn, text='Agregar',font=('Great Vibes', 15),bg='azure')
    BtnA.place(relx=.87,rely=.15,)
    BtnM = tk.Button(FrameAn, text='Modificar',font=('Great Vibes', 15),bg='azure')
    BtnM.place(relx=.87,rely=.4,)
    BtnE = tk.Button(FrameAn, text='Eliminar',font=('Great Vibes', 15),bg='azure')
    BtnE.place(relx=.87,rely=.7)
    BtnAt = tk.Button(FrameAn,text='Atras',font=('Great Vibes', 15),bg='azure',command=AtrasC)
    BtnAt.place(relx=.01,rely=.1)
    ###################################
    FrameRaza = tk.Frame(FondoC,bg='light gray')
    FrameRaza.place(relwidth=.5,height=545,y=200)

    F1 = tk.Button(FrameRaza,text='San Pedreño',bg='azure',font=('Great Vibes', 15))
    F1.place(rely=.1,x=50,relwidth=.8,height=80)

    F2 = tk.Button(FrameRaza,text='Zungo',font=('Great Vibes', 15),bg='azure')
    F2.place(rely=.4,x=50,relwidth=.8,height=80)

    F3 = tk.Button(FrameRaza,text='Casco de Mula',font=('Great Vibes', 15),bg='azure')
    F3.place(rely=.7,x=50,relwidth=.8,height=80)
    #####################
    FrameG = tk.Frame(FondoC,bg='azure')
    FrameG.place(relwidth=.5,relheight=1,y=200,relx=.5)
    GridV = ttk.Treeview(FrameG, columns=("Raza","Edad","Peso","Numero oreja","Produccion"))
    GridV.column("#0", width=10)
    GridV.column("Raza", width=200)
    GridV.column("Edad",width=50)
    GridV.column("Peso",width=50)
    GridV.column("Numero oreja",width=100)
    GridV.heading("Raza", text='Raza')
    GridV.heading("Edad", text='Edad\n(meses)')
    GridV.heading("Peso", text="Peso\n(kilos)")
    GridV.heading("Numero oreja", text='Numero oreja')
    GridV.heading("Produccion", text='Produccion\n(Diaria)')
    GridV.place(x=0,y=0,relheight=1,width=680)
    #####################
    VPrincipal.mainloop()
##############################
def VGCa(event):
    global FondoCa
    fondo.destroy()
    FondoCa = tk.Frame(VPrincipal)
    FondoCa.place(relheight=1,relwidth=1)
    ######################################
    FrameAn = tk.Frame(FondoCa,bg='green3')
    FrameAn.place(relwidth=1,height=200)

    LRaza = tk.Label(FrameAn,text='Raza:',bg='green3',font=('Great Vibes', 25))
    LRaza.place(relx=.1,rely=.3)
    CoRaza = ttk.Combobox(FrameAn, values=['Saanen','Toggenburg','Alpina','La Mancha'],font=('Great Vibes', 25))
    CoRaza.place(relx=.1,rely=.5,width=200)

    LEdad = tk.Label(FrameAn, text='Edad:(meses)', bg='green3',font=('Great Vibes', 25))
    LEdad.place(relx=.3,rely=.3)
    InEdad = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InEdad.place(relx=.3,rely=.5,width=100)

    LPeso = tk.Label(FrameAn, text='Peso:(Kilos)', bg='green3',font=('Great Vibes', 25))
    LPeso.place(relx=.5,rely=.3)
    InPeso = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InPeso.place(relx=.5,rely=.5,width=100)

    LNum = tk.Label(FrameAn, text='Numero Oreja:', bg='green3',font=('Great Vibes', 25))
    LNum.place(relx=.7,rely=.3)
    InNum = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InNum.place(relx=.7,rely=.5,width=200)
    
    BtnA = tk.Button(FrameAn, text='Agregar',font=('Great Vibes', 15),bg='azure')
    BtnA.place(relx=.87,rely=.15,)
    BtnM = tk.Button(FrameAn, text='Modificar',font=('Great Vibes', 15),bg='azure')
    BtnM.place(relx=.87,rely=.4,)
    BtnE = tk.Button(FrameAn, text='Eliminar',font=('Great Vibes', 15),bg='azure')
    BtnE.place(relx=.87,rely=.7)
    BtnAt = tk.Button(FrameAn,text='Atras',font=('Great Vibes', 15),bg='azure',command=AtrasCa)
    BtnAt.place(relx=.01,rely=.1)
    ###################################
    FrameRaza = tk.Frame(FondoCa,bg='light gray')
    FrameRaza.place(relwidth=.5,height=545,y=200)

    F1 = tk.Button(FrameRaza,text='Saanen',bg='azure',font=('Great Vibes', 15))
    F1.place(rely=.1,x=50,relwidth=.8,height=80)

    F2 = tk.Button(FrameRaza,text='Toggenburg',font=('Great Vibes', 15),bg='azure')
    F2.place(rely=.3,x=50,relwidth=.8,height=80)

    F3 = tk.Button(FrameRaza,text='Alpina',font=('Great Vibes', 15),bg='azure')
    F3.place(rely=.5,x=50,relwidth=.8,height=80)

    F4 = tk.Button(FrameRaza,text='La Mancha',font=('Great Vibes', 15),bg='azure')
    F4.place(rely=.7,x=50,relwidth=.8,height=80)
    #####################
    FrameG = tk.Frame(FondoCa,bg='azure')
    FrameG.place(relwidth=.5,relheight=1,y=200,relx=.5)
    GridV = ttk.Treeview(FrameG, columns=("Raza","Edad","Peso","Numero oreja","Produccion"))
    GridV.column("#0", width=10)
    GridV.column("Raza", width=200)
    GridV.column("Edad",width=50)
    GridV.column("Peso",width=50)
    GridV.column("Numero oreja",width=100)
    GridV.heading("Raza", text='Raza')
    GridV.heading("Edad", text='Edad\n(meses)')
    GridV.heading("Peso", text="Peso\n(kilos)")
    GridV.heading("Numero oreja", text='Numero oreja')
    GridV.heading("Produccion", text='Produccion\n(Diaria)')
    GridV.place(x=0,y=0,relheight=1,width=680)
    #####################
    VPrincipal.mainloop()
##############################
def VGG(event):
    global FondoGa
    fondo.destroy()
    FondoGa = tk.Frame(VPrincipal)
    FondoGa.place(relheight=1,relwidth=1)
    ####################################
    FrameAn = tk.Frame(FondoGa,bg='green3')
    FrameAn.place(relwidth=1,height=200)

    LRaza = tk.Label(FrameAn,text='Raza:',bg='green3',font=('Great Vibes', 25))
    LRaza.place(relx=.1,rely=.3)
    CoRaza = ttk.Combobox(FrameAn, values=['Leghorn Blanca','Rhode Island Roja','New Hampshire','Cornish','Sussex Clara'],font=('Great Vibes', 25))
    CoRaza.place(relx=.1,rely=.5,width=200)

    LEdad = tk.Label(FrameAn, text='Edad:(meses)', bg='green3',font=('Great Vibes', 25))
    LEdad.place(relx=.3,rely=.3)
    InEdad = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InEdad.place(relx=.3,rely=.5,width=100)

    LPeso = tk.Label(FrameAn, text='Peso:(Kilos)', bg='green3',font=('Great Vibes', 25))
    LPeso.place(relx=.5,rely=.3)
    InPeso = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InPeso.place(relx=.5,rely=.5,width=100)

    LNum = tk.Label(FrameAn, text='Numero Oreja:', bg='green3',font=('Great Vibes', 25))
    LNum.place(relx=.7,rely=.3)
    InNum = tk.Entry(FrameAn,font=('Great Vibes', 25))
    InNum.place(relx=.7,rely=.5,width=200)
    
    BtnA = tk.Button(FrameAn, text='Agregar',font=('Great Vibes', 15),bg='azure')
    BtnA.place(relx=.87,rely=.15,)
    BtnM = tk.Button(FrameAn, text='Modificar',font=('Great Vibes', 15),bg='azure')
    BtnM.place(relx=.87,rely=.4,)
    BtnE = tk.Button(FrameAn, text='Eliminar',font=('Great Vibes', 15),bg='azure')
    BtnE.place(relx=.87,rely=.7)
    BtnAt = tk.Button(FrameAn,text='Atras',font=('Great Vibes', 15),bg='azure',command=AtrasGa)
    BtnAt.place(relx=.01,rely=.1)
    ###################################
    FrameRaza = tk.Frame(FondoGa,bg='light gray')
    FrameRaza.place(relwidth=.5,height=545,y=200)

    F1 = tk.Button(FrameRaza,text='Leghorn Blanca',bg='azure',font=('Great Vibes', 15))
    F1.place(rely=.03,x=50,relwidth=.8,height=80)

    F2 = tk.Button(FrameRaza,text='Rhode Island Roja',font=('Great Vibes', 15),bg='azure')
    F2.place(rely=.23,x=50,relwidth=.8,height=80)

    F3 = tk.Button(FrameRaza,text='New Hampshire',font=('Great Vibes', 15),bg='azure')
    F3.place(rely=.43,x=50,relwidth=.8,height=80)

    F4 = tk.Button(FrameRaza,text='Cornish',font=('Great Vibes', 15),bg='azure')
    F4.place(rely=.63,x=50,relwidth=.8,height=80)

    F5 = tk.Button(FrameRaza,text='Sussex Clara',font=('Great Vibes', 15),bg='azure')
    F5.place(rely=.83,x=50,relwidth=.8,height=80)
    #####################
    FrameG = tk.Frame(FondoGa,bg='azure')
    FrameG.place(relwidth=.5,relheight=1,y=200,relx=.5)
    GridV = ttk.Treeview(FrameG, columns=("Raza","Edad","Peso","Numero oreja","Produccion"))
    GridV.column("#0", width=10)
    GridV.column("Raza", width=200)
    GridV.column("Edad",width=50)
    GridV.column("Peso",width=50)
    GridV.column("Numero oreja",width=100)
    GridV.heading("Raza", text='Raza')
    GridV.heading("Edad", text='Edad\n(meses)')
    GridV.heading("Peso", text="Peso\n(kilos)")
    GridV.heading("Numero oreja", text='Numero oreja')
    GridV.heading("Produccion", text='Produccion\n(Diaria)')
    GridV.place(x=0,y=0,relheight=1,width=680)
    #####################
    VPrincipal.mainloop()
##############################
def VCultivo():
    FondoCu = tk.Frame(VPrincipal, bg='light grey')
    FondoCu.place(relheight=1, relwidth=1)
##############################
def VTotal(event):
    pass
##############################
def Salir(event):
    pass
##############################
def AtrasC():
    FondoC.destroy()
    VGanado()
def AtrasV():
    FondoV.destroy()
    VGanado()
def AtrasCa():
    FondoCa.destroy()
    VGanado()
def AtrasGa():
    FondoGa.destroy()
    VGanado()
##############################
def AtrasG():
    fondo.destroy()
    Vprincipal()
##############################
def Vprincipal():
    global Background

    #################################################
    Background = tk.Frame(VPrincipal, bg='light grey')
    Background.place(relheight=1, relwidth=1)
    ##################################################
    FrameHead = tk.Frame(VPrincipal, bg='light grey')
    FrameHead.place(x=0, y=0, relwidth=1, height=60)
    FPL = tk.Label(FrameHead, text='Granja Ucundinamarca', font=('Great Vibes', 25), bg='light grey')
    FPL.place(x=20, y=20)

    ##################################################

    FrameCul = tk.Frame(VPrincipal, bg='azure',)
    FrameCul.place(x=150, y=100, width=300, height=550)
    FrameCul.config(highlightbackground="black", highlightthickness=1)

    icul = Image.open('imagenes/cul.png')
    icul = icul.resize((250, 250))
    icul = ImageTk.PhotoImage(icul)
    CulL1 = tk.Label(FrameCul, image=icul, bg='azure')
    CulL1.place(x=0, y=50, width=290, height=290)
    CulL2 = tk.Label(FrameCul, text='CULTIVOS', bg='azure', anchor='center', font=('Great Vibes', 25))
    CulL2.place(relwidth=1, rely=.7)

    FrameCul.bind("<Button-1>", VCul)
    CulL1.bind("<Button-1>", VCul)
    CulL2.bind("<Button-1>", VCul)
    #######################################

    FrameGan = tk.Frame(VPrincipal, bg='azure')
    FrameGan.place(x=550, y=100, width=300, height=550)
    FrameGan.config(highlightbackground="black", highlightthickness=1)

    iGan = Image.open('imagenes/Gan.png')
    iGan = iGan.resize((300, 300))
    iGan = ImageTk.PhotoImage(iGan)
    GanL1 = tk.Label(FrameGan, image=iGan, bg='azure')
    GanL1.place(x=0, y=50, width=290, height=290)
    GanL2 = tk.Label(FrameGan, text='GANADO', bg='azure', anchor='center', font=('Great Vibes', 25))
    GanL2.place(relwidth=1, rely=.7)

    FrameGan.bind("<Button-1>", Vgan)
    GanL1.bind("<Button-1>", Vgan)
    GanL2.bind("<Button-1>", Vgan)
    ########################################

    FrameTo = tk.Frame(VPrincipal, bg='azure')
    FrameTo.place(x=950, y=100, width=300, height=550)
    FrameTo.config(highlightbackground="black", highlightthickness=1)

    iTo = Image.open('imagenes/total.png')
    iTo = iTo.resize((400, 400))
    iTo = ImageTk.PhotoImage(iTo)
    ToL1 = tk.Label(FrameTo, image=iTo, bg='azure')
    ToL1.place(x=0, y=50, width=290, height=290)
    ToL2 = tk.Label(FrameTo, text='REPORTE', bg='azure', anchor='center', font=('Great Vibes', 25))
    ToL2.place(relwidth=1, rely=.7)

    FrameTo.bind("<Button-1>", VTotal)
    ToL2.bind("<Button-1>", VTotal)
    ToL1.bind("<Button-1>", VTotal)
    VPrincipal.mainloop()
##############################
def Vgan(event):
    Background.destroy()
    VGanado()
def VCul(event):
    Background.destroy()
    VCultivo()
DATABASE = 'Granja'
try:
    cnn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'Server=KAKAROTTO639\SQLEXPRESS;'
        'DATABASE='+DATABASE+';'
        'Trusted_Connection=yes;'
    )
    print('conexion exitosa')
except pyodbc.Error as e:
    messagebox.showerror("Error", f"No se pudo Conectar al servidor: {e}")
except Exception as ex:
    messagebox.showerror("Error", f"Se ha producido un error: {ex}")

##############################
if __name__ == "__main__":
    VPrincipal = tk.Tk()
    VPrincipal.title('Granja Ucundinamarca')
    VPrincipal.state('zoomed')
    Vprincipal()
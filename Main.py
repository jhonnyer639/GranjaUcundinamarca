from tkinter import ttk, messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pyodbc

def VGanado(event):
    global Vganado
    Vganado =  tk.Tk()
    Vganado.title('Granja Ucundinamarca')
    Vganado.state('zoomed')
    VPrincipal.destroy()
    #####################
    Background = tk.Frame(Vganado, bg='light grey')
    Background.place(relheight=1, relwidth=1)
    ##########################################
    FrameHead = tk.Frame(Background, bg='green3')
    FrameHead.place(x=0, y=0, relwidth=1, height=60)
    FPL = tk.Label(FrameHead, text='Ganado de  la Granja Ucundinamarca', font=('Great Vibes', 25), bg='green3', fg='white')
    FPL.place(x=20, y=20)
    ######################
    FrameRe = tk.Frame(Background, bg='slate grey')
    FrameRe.place(y=60,height=200,relwidth=1)
    ######################
    FrameEs = tk.Frame(Background,bg='light grey')
    FrameEs.place(relwidth=1,height=500,y=260)

    Esp1L = tk.Label(FrameEs,text='Bovinos',bg='grey')
    Esp1L.place(x=20,y=20,relwidth=.45,height=100)

    Esp2L = tk.Label(FrameEs,text='Porcinos',bg='grey')
    Esp2L.place(x=20,y=140,relwidth=.45,height=100)

    Esp3L = tk.Label(FrameEs,text='Caprino',bg='grey')
    Esp3L.place(relx=.5,y=140,relwidth=.45,height=100)

    Esp4L = tk.Label(FrameEs,text='Avicultura',bg='grey')
    Esp4L.place(x=20,y=260,relwidth=.45,height=100)

    Esp5L = tk.Label(FrameEs,text='Avicultura',bg='grey')
    Esp5L.place(relx=.5,y=20,relwidth=.45,height=100)

    B_Atraz = tk.Button(Background, text='Atraz',bg='green3',command=AtrazG)
    B_Atraz.place(y=680,x=30,width=50,height=25)


def VCultivo(event):
    pass

def VTotal(event):
    pass

def AtrazG():
    Vprincipal()
    Vganado.destroy()

def Vprincipal():
    global VPrincipal
    VPrincipal = tk.Tk()
    VPrincipal.title('Granja Ucundinamarca')
    VPrincipal.state('zoomed')

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

    FrameCul.bind("<Button-1>", VCultivo)
    CulL1.bind("<Button-1>", VCultivo)
    CulL2.bind("<Button-1>", VCultivo)
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

    FrameGan.bind("<Button-1>", VGanado)
    GanL1.bind("<Button-1>", VGanado)
    GanL2.bind("<Button-1>", VGanado)
    ########################################

    FrameTo = tk.Frame(VPrincipal, bg='azure')
    FrameTo.place(x=950, y=100, width=300, height=550)
    FrameTo.config(highlightbackground="black", highlightthickness=1)

    iTo = Image.open('imagenes/total.png')
    iTo = iTo.resize((400, 400))
    iTo = ImageTk.PhotoImage(iTo)
    ToL1 = tk.Label(FrameTo, image=iTo, bg='azure')
    ToL1.place(x=0, y=50, width=290, height=290)
    ToL2 = tk.Label(FrameTo, text='Resumen', bg='azure', anchor='center', font=('Great Vibes', 25))
    ToL2.place(relwidth=1, rely=.7)

    FrameTo.bind("<Button-1>", VTotal)
    ToL2.bind("<Button-1>", VTotal)
    ToL1.bind("<Button-1>", VTotal)

    VPrincipal.mainloop()


######################

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

#########################
if __name__ == "__main__":
    Vprincipal()
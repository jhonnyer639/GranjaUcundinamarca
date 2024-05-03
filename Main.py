from tkinter import ttk , messagebox
from tkinter import *
import tkinter as tk

from PIL import ImageTk , Image
import pyodbc

def Ganad():
    pass
def Cultivo():
    pass
def Total():
    pass


def main():
    VPrinsipal = tk.Tk()
    VPrinsipal.title('Granja Ucundinamarca')
    VPrinsipal.state('zoomed')

    ##################################################
    FrameHead = tk.Frame(VPrinsipal, bg='ghost white')
    FrameHead.place(x= 0, y= 0, relwidth= 1, height= 60)
    FPL = tk.Label(FrameHead,text='Granja Ucundinamarca',font=('Great Vibes', 25), bg='ghost white')
    FPL.place(x=20,y=20)

    ##################################################

    FrameEHead = tk.Frame(VPrinsipal, bg='green4')
    FrameEHead.place(x= 0, y= 60, relwidth= 1, height= 160)
    TL = tk.Label(FrameEHead, text='Total',font=('Great Vibes', 50),bg='green4')
    TL.place(x=570,y=40)

    ##################################################

    FrameCul = tk.Frame(VPrinsipal, bg='green3')
    FrameCul.place(x=200,y=280,width=300,height=400)

    icul = Image.open('imagenes/cul.png')
    icul = icul.resize((100,140))
    icul = ImageTk.PhotoImage(icul)
    CulL1 = tk.Label(FrameCul, image=icul)
    CulL1.place(relx=.25,y=50,relwidth=.5,height=140)
    CulL2 = tk.Label(FrameCul, text='CULTIVOS', bg='green3', anchor='center', font=('Great Vibes', 25))
    CulL2.place(relx=.25,rely=.7)
    
    FrameGan = tk.Frame(VPrinsipal, bg='green3')
    FrameGan.place(x=850,y=280,width=300,height=400)

    iGan = Image.open('imagenes/Gan.png')
    iGan = iGan.resize((100,140))
    iGan = ImageTk.PhotoImage(iGan)
    GanL1 = tk.Label(FrameGan, image=iGan)
    GanL1.place(relx=.25,y=50,relwidth=.5,height=140)
    GanL2 = tk.Label(FrameGan, text='GANADO', bg='green3', anchor='center', font=('Great Vibes', 25))
    GanL2.place(relx=.3,rely=.7)




    VPrinsipal.mainloop()


DATABASE = 'Granja'
try:

    cnn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'Server=KAKAROTTO639\SQLEXPRESS;'
        'DATABASE='+DATABASE+';'
        'Trusted_Connection=yes;'
        )
    print('conexion exitosa')
except:
    messagebox.showerror("Error", f"No se pudo Conectar al servidor: ")

if __name__ == "__main__":
    main()
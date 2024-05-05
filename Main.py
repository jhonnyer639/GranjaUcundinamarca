from tkinter import ttk , messagebox
from tkinter import *
import tkinter as tk

from PIL import ImageTk , Image
from PIL import *
import pyodbc


class Aplicacion(tk.Tk):
    def Ganad(self):
        print('hello')
        pass
    def Cultivo(self):
        pass
    def Total(self):
        pass


    def Crear_widgets(self):
        #self.VPrinsipal = tk.Tk()
        #self.VPrinsipal.title('Granja Ucundinamarca')
        #self.VPrinsipal.state('zoomed')

        ##################################################
        self.Bacground = tk.Frame(self, bg='light grey')
        self.Bacground.place(relheight=1,relwidth=1)
        ##################################################
        self.FrameHead = tk.Frame(self, bg='light grey')
        self.FrameHead.place(x= 0, y= 0, relwidth= 1, height= 60)
        self.FPL = tk.Label(self.FrameHead,text='Granja Ucundinamarca',font=('Great Vibes', 25), bg='light grey')
        self.FPL.place(x=20,y=20)

        ##################################################

        self.FrameCul = tk.Frame(self, bg='azure',)
        self.FrameCul.place(x=150,y=100,width=300,height=550)
        self.FrameCul.config(highlightbackground="black", highlightthickness=1)

        self.icul = Image.open('imagenes/cul.png')
        self.icul = self.icul.resize((250,250))
        self.icul = ImageTk.PhotoImage(self.icul)
        self.CulL1 = tk.Label(self.FrameCul, image=self.icul,bg='azure',command=self.Ganad)
        self.CulL1.place(x=0,y=50,width=290,height=290)
        self.CulL2 = tk.Label(self.FrameCul, text='CULTIVOS', bg='azure', anchor='center', font=('Great Vibes', 25))
        self.CulL2.place(relwidth=1,rely=.7)
        
        self.FrameGan = tk.Frame(self, bg='azure')
        self.FrameGan.place(x=550,y=100,width=300,height=550)
        self.FrameGan.config(highlightbackground="black", highlightthickness=1)

        self.iGan = Image.open('imagenes/Gan.png')
        self.iGan = self.iGan.resize((300,300))
        self.iGan = ImageTk.PhotoImage(self.iGan)
        self.GanL1 = tk.Label(self.FrameGan, image=self.iGan, bg='azure')
        self.GanL1.place(x=0,y=50,width=290,height=290)
        self.GanL2 = tk.Label(self.FrameGan, text='GANADO', bg='azure', anchor='center', font=('Great Vibes', 25))
        self.GanL2.place(relwidth=1,rely=.7)

        self.FrameTo = tk.Frame(self, bg='azure')
        self.FrameTo.place(x=950,y=100,width=300,height=550)
        self.FrameTo.config(highlightbackground="black", highlightthickness=1)

        self.iTo = Image.open('imagenes/total.png')
        self.iTo = self.iTo.resize((400,400))
        self.iTo = ImageTk.PhotoImage(self.iTo)
        self.ToL1 = tk.Label(self.FrameTo, image=self.iTo, bg='azure')
        self.ToL1.place(x=0,y=50,width=290,height=290)
        self.ToL2 = tk.Label(self.FrameTo, text='Resumen', bg='azure', anchor='center', font=('Great Vibes', 25))
        self.ToL2.place(relwidth=1,rely=.7)
        
        self.mainloop()



app = Aplicacion()
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
    app.Crear_widgets()
import pygame, sys,pyttsx3,datetime
import subprocess as sub
from pygame.locals import *
import speech_recognition as sr
from tkinter import filedialog
import tkinter as tk

pygame.init()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
Voz=True
name = "Speakos"
listener = sr.Recognizer()

sites = {
            'google':'chrome.exe',
            'word':''
}

pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def talk(text):
    engine.say(text)
    engine.runAndWait()

ANCHO, ALTO = pantalla.get_size()
talk("iniciando speak OS")

tk.Tk().withdraw()

def listen():
    try:
        with sr.Microphone() as sourse:
            print("Escuchando...")
            PC= listener.listen(sourse)
            rec = listener.recognize_google(PC, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
    return rec

def cambiar_fondo():
    archivo = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Imagen PNG,JPG,JPEG", "*.png;*.jpg;*.jpeg"), ("Todos los archivos", "*.*")])
    if archivo:
        return pygame.image.load(archivo)
    return None

fondo = pygame.image.load("image.png")
if fondo:
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL_CLARO = (173, 216, 230)

pygame.font.init()
fuente = pygame.font.SysFont("Arial", 32)

# Cargar la imagen del botón
imagen_boton = pygame.image.load('IcoMenu.png')
imagen_boton = pygame.transform.scale(imagen_boton, (100, 100))

imagen_alta = pygame.image.load('altavoz.png')
imagen_alta = pygame.transform.scale(imagen_alta, (100, 100))

imagen_word = pygame.image.load("word.png")
imagen_word = pygame.transform.scale(imagen_word,(100,100))

imagen_excel = pygame.image.load("excel.png")
imagen_excel = pygame.transform.scale(imagen_excel,(100,100))

imagen_power = pygame.image.load("power.png")
imagen_power = pygame.transform.scale(imagen_power,(100,100))

imagen_crhome = pygame.image.load("crhome.png")
imagen_crhome = pygame.transform.scale(imagen_crhome,(100,100))

imagen_bpower = pygame.image.load("bpower.png")
imagen_bpower = pygame.transform.scale(imagen_bpower,(60,50))


# Variable para la imagen grande
imagen_grande = None

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            corriendo = False
        # Cambiar el fondo cuando se presiona la tecla 'f'
        if evento.type == KEYDOWN and evento.key == K_f:
            fondo = cambiar_fondo()
            if fondo:
                fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        # Ocultar la imagen grande al presionar la tecla 'Escape'
        if evento.type == KEYDOWN and evento.key == K_ESCAPE:
            if imagen_grande != None:
                imagen_grande = None
                imagen_ajustes = None
                if Voz == True:
                    talk("Cerrando menu")
                else:
                    pass

        # Detectar clic del mouse
        if evento.type == MOUSEBUTTONDOWN:
            if evento.button == 1:  # Clic izquierdo
                mouse_post = pygame.mouse.get_pos()

                imagen_rect = imagen_boton.get_rect(center=(x_circulo + 200 // 2, y_circulo + 200 // 2))
                imagen_rect1 = imagen_alta.get_rect(center = (10 , ALTO - 100))
                Hora = texto_hora.get_rect(center = (55, 125))
                Dia = texto_Dia.get_rect(center=(ANCHO - ancho_texto_Dia - 40, 130))
                Fecha = texto_fecha.get_rect(center=(ANCHO - ancho_texto_fecha - 25, 160))
                Apagar = imagen_bpower.get_rect(center=(ANCHO - 100 + 30,ALTO -50 + 25))
                
                word = imagen_word.get_rect(center=(60,240))
                excel = imagen_excel.get_rect(center=(210,230))
                power = imagen_power.get_rect(center=(60,360))
                chrome = imagen_crhome.get_rect(center=(210,360))

                if imagen_rect.collidepoint(mouse_post): #abrir menu
                    if imagen_grande == None:
                        imagen_grande = pygame.image.load('descarga.png')
                        imagen_grande = pygame.transform.scale(imagen_grande, (600, 600))
                        imagen_ajustes = pygame.image.load("ajustes.png")
                        imagen_ajustes = pygame.transform.scale(imagen_ajustes,(60,50))
                        imagen_pc = pygame.image.load("pc.png")
                        imagen_pc = pygame.transform.scale(imagen_pc,(60,50))
                        imagen_wiffi = pygame.image.load("wiffi.png")
                        imagen_wiffi = pygame.transform.scale(imagen_wiffi,(60,50))
                        imagen_blue = pygame.image.load("blue.png")
                        imagen_blue = pygame.transform.scale(imagen_blue,(60,50))
                        
                        if Voz == True:
                            talk("Abriendo menu")
                        else:
                            pass
                if imagen_rect1.collidepoint(mouse_post): #cerrar menu
                    if Voz == True:
                        talk("Narrador de voz desactivado")
                        Voz = False
                    else:
                        talk("Narrador de voz Activado")
                        Voz = True
                if Hora.collidepoint(mouse_post):
                    if Voz == True:
                        talk(hora_actual)
                if Dia.collidepoint(mouse_post):
                    if Voz == True:
                        talk(datetime.datetime.now().strftime('%d-%m-%y'))
                if Fecha.collidepoint(mouse_post):
                    if Voz == True:
                        talk(datetime.datetime.now().strftime('%d-%m-%y'))
                if Apagar.collidepoint(mouse_post):
                    if Voz == True:
                        talk("apagando equipo")
                    else:
                        pass
                    pygame.quit()
                    sys.exit()
                
                    if Voz == True:
                        talk("abriendo bluethoot")
                if word.collidepoint(mouse_post):
                    if Voz == True:
                        talk("abriendo word")
                    sub.call(f'start WINWORD.EXE', shell=True)
                if excel.collidepoint(mouse_post):
                    if Voz == True:
                        talk("abriendo excel")
                    sub.call(f'start EXCEL.EXE', shell=True)
                if power.collidepoint(mouse_post):
                    if Voz == True:
                        talk("abriendo powerpoint")
                    sub.call(f'start POWERPNT.EXE', shell=True)
                if chrome.collidepoint(mouse_post):
                    if Voz == True:
                        talk("abriendo chrome")
                    
        

    # Obtener la hora actual
    hora_actual = datetime.datetime.now().strftime('%H:%M')
    texto_hora = fuente.render(hora_actual, True, BLANCO)
    Dia_actual = datetime.datetime.now().strftime('%d')
    texto_Dia = fuente.render(Dia_actual, True, BLANCO)
    fecha_actual = datetime.datetime.now().strftime('%m-%y')
    texto_fecha = fuente.render(fecha_actual, True, BLANCO)

    if fondo:
        pantalla.blit(fondo, (0, 0))
    else:
        pantalla.fill(BLANCO)


    x_circulo = (ANCHO - 200) // 2
    y_circulo = (ALTO - 200) // 2
    superficie_circulo = pygame.Surface((200, 200), pygame.SRCALPHA)
    superficie_circulo.fill((0, 0, 0, 0))
    pygame.draw.ellipse(superficie_circulo, BLANCO, (0, 0, 100, 100), 2)
    pygame.draw.ellipse(superficie_circulo, (173, 216, 230, 150), (0, 0, 100, 100)) 

    imagen_rect = imagen_boton.get_rect(center=(x_circulo + 200 // 2, y_circulo + 200 // 2))

    pantalla.blit(imagen_boton, imagen_rect)
    pantalla.blit(imagen_alta, (10 , ALTO - 100))
    pantalla.blit(imagen_word,(50,220))
    pantalla.blit(imagen_excel,(200,220))
    pantalla.blit(imagen_power,(50,350))
    pantalla.blit(imagen_crhome,(200,350))
    pantalla.blit(imagen_bpower,(ANCHO - 100,ALTO -50))
    

    if imagen_grande:
        grande_rect = imagen_grande.get_rect(center=(ANCHO // 2, ALTO // 2))  # Centrar la imagen grande
        pantalla.blit(imagen_grande, grande_rect)
        pantalla.blit(imagen_ajustes,(ANCHO//2 + 20,(ALTO/2)-150))
        pantalla.blit(imagen_pc,(ANCHO//2 - 80,(ALTO/2)-150))
        pantalla.blit(imagen_wiffi,(ANCHO//2 - 145,(ALTO/2)-80))
        pantalla.blit(imagen_blue,(ANCHO//2 - 145,(ALTO/2 +5)))

    pantalla.blit(texto_hora, (50, 120))  
    ancho_texto_Dia = texto_fecha.get_width()
    pantalla.blit(texto_Dia, (ANCHO - ancho_texto_Dia - 20, 120))
    ancho_texto_fecha = texto_fecha.get_width()
    pantalla.blit(texto_fecha, (ANCHO - ancho_texto_fecha - 35, 150))

    # Actualizar pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()

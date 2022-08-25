import pyautogui
from time import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame


# ----------------------------------------- LikeStory by @thiisp 1 tela -----------------------------------------


def LikeStory1():
    pyautogui.PAUSE = 0.350
    pyautogui.press('win')
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    sleep(1)
    # pyautogui.doubleClick(x=-906, y=28) <~ caso o navegador abra sem estar maximizado.
    pyautogui.click(x=469, y=51)
    pyautogui.write('instagram.com')
    pyautogui.press('enter')
    sleep(6)
    pyautogui.click(x=312, y=206)

    count = 0

    while count < 10000:
        pyautogui.click(x=772, y=666)
        pyautogui.click(x=876, y=399)

# ----------------------------------------- LikeStory by @thiisp 2 tela -----------------------------------------


def LikeStory2():
    pyautogui.PAUSE = 0.350
    pyautogui.press('win')
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    sleep(1)
    # pyautogui.doubleClick(x=-906, y=28) <~ caso o navegador abra sem estar maximizado.
    pyautogui.click(x=-1035, y=49)
    pyautogui.write('instagram.com')
    pyautogui.press('enter')
    sleep(5)
    pyautogui.click(x=-1054, y=203)

    count = 0

    while count < 10000:
        pyautogui.click(x=-592, y=663)
        pyautogui.click(x=-493, y=395)

# ----------------------------------------- Visualizar Story -----------------------------------------


def VisualizarStory():
    pyautogui.PAUSE = 0.25
    pyautogui.press('win')
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    sleep(1)
    #pyautogui.doubleClick(x=-906, y=28)
    pyautogui.click(x=469, y=51)
    pyautogui.write('instagram.com')
    pyautogui.press('enter')
    sleep(7)
    pyautogui.click(x=312, y=206)

    count = 0

    while count < 10000:
        pyautogui.click(x=876, y=399)

# ----------------------------------------- Criador -----------------------------------------


def Criador():
    pyautogui.PAUSE = 1
    pyautogui.press('win')
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write('instagram.com/thiisp')
    pyautogui.press('enter')

# ----------------------------------------- Música -----------------------------------------


pygame.mixer.init()


def play():
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play(loops=10)


def stop():
    pygame.mixer.music.stop()

# ----------------------------------------- Comandos -----------------------------------------


font = 'arial 10 bold'

# ----------------------------------------- Programa by @thiisp -----------------------------------------
root = Tk()


class aplicativoThiisp():
    def __init__(self):
        self.root = root
        self.tela()
        self.background()
        self.aviso()
        self.titulo()
        self.textos()
        self.botoes()
        self.criador()
        self.musica()
        root.mainloop()

    def tela(self):
        self.root.title('Instagram Mod by @thiisp')
        self.root.geometry('500x500')
        self.root.attributes('-alpha', 0.92)
        self.root.resizable(False, False)

    def background(self):
        imagemAnonymous = Image.open('anonymous.png')
        img = ImageTk.PhotoImage(imagemAnonymous)
        background = Label(image=img)
        background.image = img
        background.place(x=0, y=0)

    def aviso(self):
        messagebox.showwarning(
            'AVISO !!!!', 'Esse aplicativo foi desenvolvido por @thiisp, caso você tenha baixado por alguem sem ser o próprio Thiago, DESINSTALE IMEDIATAMENTE!!!')
        messagebox.showerror(
            'Tome Cuidado!', 'LEMBRE-SE DISSO: Para desativar o clicker você deverá apertar "CTRL + ALT + DEL".')

    def titulo(self):
        titulo = Label(root,
                       text='Menu Instagram',
                       bg='black',
                       fg='red',
                       font='arial 20 bold')
        titulo.place(x=150, y=20)

    def textos(self):
        textoLike = Label(root, text='Mod Curtir Storys Auto',
                          bg='black', fg='red', font=font)
        textoLike.place(x=20, y=90)

        textoVisualizar = Label(
            root, text='Mod Auto Visualizar Storys', bg='black', fg='red', font=font)
        textoVisualizar.place(x=300, y=90)

        textoAumentarVelocidade = Entry(root,)

    def botoes(self):
        botaoLike = Button(root, text='Clique Aqui!', bg='blue',
                           fg='white', font='arial 9 bold', command=LikeStory1)
        botaoLike.place(x=60, y=120)

        botaoVisualizar = Button(
            root, text='Clique Aqui!', bg='blue', fg='white', font='arial 9 bold', command=VisualizarStory)
        botaoVisualizar.place(x=300, y=120)

    def criador(self):
        criador = Label(root, text='Instagram do Criador:',
                        bg='black', fg='white', font='arial 12 bold')
        criador.place(x=5, y=473)

        botaoCriador = Button(root, text='@Thiisp', bg='black',
                              fg='blue', font='arial 9 bold', command=Criador)
        botaoCriador.place(x=180, y=473)

    def musica(self):
        botaoMusica = Button(root, text='Tocar Música', bg='black',
                             fg='red', font='arial 9 bold', command=play)
        botaoMusica.place(x=307, y=473)

        botaoStop = Button(root, text='Desligar Música', bg='black',
                           fg='red', font='arial 9 bold', command=stop)
        botaoStop.place(x=395, y=473)


aplicativoThiisp()

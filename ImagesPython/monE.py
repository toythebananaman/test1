from tkinter import *
import subprocess

FenetreP = Tk()
FenetreP.title('Photoshoper')


def create_window():
    new_window = Tk()

def nProjet():
    # Application de l'effet grâce à un autre programme
    subprocess.call("python ./scripts/save.py")



Button(FenetreP,text="nouveau Projet",command=create_window).pack(side = LEFT, padx = 50, pady = 50)

Bouton2 = Button1(FenetreP, text='Quitter', command=FenetreP.destroy)
Bouton2.pack(side = RIGHT, padx = 50, pady = 50)








FenetreP.mainloop()
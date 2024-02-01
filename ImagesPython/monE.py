from tkinter import *
import subprocess

FenetreP = Tk()
FenetreP.title('Photoshoper')

def create_window():
    new_window = Toplevel()

def nProjet():
    subprocess.call(["python", "./scripts/save.py"])

Button(FenetreP, text="Nouveau Projet", command=create_window).pack(side=LEFT, padx=50, pady=5)

Bouton2 = Button(FenetreP, text='Quitter', command=FenetreP.quit)
Bouton2.pack(side=RIGHT, padx=50, pady=5)

FenetreP.mainloop()

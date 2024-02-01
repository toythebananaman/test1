from tkinter import *
import subprocess

def undo():
    # Application de l'effet grâce à un autre programme
    subprocess.call("python ./scripts/undo.py")

       # Mise à jour de la photo (modifiée) dans le canevas
    global item, Canevas, Mafenetre, photo
    Canevas.delete(ALL)
    photo = PhotoImage(file="image.png")
    #Canevas.itemconfig(item,image=photo)
    item = Canevas.create_image(0,0,anchor=NW, image=photo)
    print("Image de fond (item",item,")")
    Canevas.pack()

def restart():
    # Application de l'effet grâce à un autre programme
    subprocess.call("python ./scripts/restart.py")

       # Mise à jour de la photo (modifiée) dans le canevas
    global item, Canevas, Mafenetre, photo
    Canevas.delete(ALL)
    photo = PhotoImage(file="./image.png")
    #Canevas.itemconfig(item,image=photo)
    item = Canevas.create_image(0,0,anchor=NW, image=photo)
    print("Image de fond (item",item,")")
    Canevas.pack()

def negatif():
    # Application de l'effet grâce à un autre programme
    subprocess.call("python ./scripts/negatif.py")

       # Mise à jour de la photo (modifiée) dans le canevas
    global item, Canevas, Mafenetre, photo
    Canevas.delete(ALL)
    photo = PhotoImage(file="image.png")
    #Canevas.itemconfig(item,image=photo)
    item = Canevas.create_image(0,0,anchor=NW, image=photo)
    print("Image de fond (item",item,")")
    Canevas.pack()

def banane():
    # Application de l'effet grâce à un autre programme
    subprocess.call("python ./scripts/banana.py")

       # Mise à jour de la photo (modifiée) dans le canevas
    global item, Canevas, Mafenetre, photo
    Canevas.delete(ALL)
    photo = PhotoImage(file="image.png")
    #Canevas.itemconfig(item,image=photo)
    item = Canevas.create_image(0,0,anchor=NW, image=photo)
    print("Image de fond (item",item,")")
    Canevas.pack()

def miroirX():
    # Application de l'effet grâce à un autre programme
    subprocess.call("python ./scripts/miroirX.py")

       # Mise à jour de la photo (modifiée) dans le canevas
    global item, Canevas, Mafenetre, photo
    Canevas.delete(ALL)
    photo = PhotoImage(file="image.png")
    #Canevas.itemconfig(item,image=photo)
    item = Canevas.create_image(0,0,anchor=NW, image=photo)
    print("Image de fond (item",item,")")
    Canevas.pack()
def miroirY():
    # Application de l'effet grâce à un autre programme
    subprocess.call("python ./scripts/miroirY.py")

       # Mise à jour de la photo (modifiée) dans le canevas
    global item, Canevas, Mafenetre, photo
    Canevas.delete(ALL)
    photo = PhotoImage(file="image.png")
    #Canevas.itemconfig(item,image=photo)
    item = Canevas.create_image(0,0,anchor=NW, image=photo)
    print("Image de fond (item",item,")")
    Canevas.pack()
def saveNquit():
    # Application de l'effet grâce à un autre programme
    subprocess.call("python ./scripts/save.py")

       # Mise à jour de la photo (modifiée) dans le canevas
    global item, Canevas, Mafenetre, photo
    Canevas.delete(ALL)
    photo = PhotoImage(file="image.png")
    #Canevas.itemconfig(item,image=photo)
    item = Canevas.create_image(0,0,anchor=NW, image=photo)
    print("Image de fond (item",item,")")
    Canevas.pack()
def imgOpen():
    # Application de l'effet grâce à un autre programme
    subprocess.call("python ./scripts/open.py")

       # Mise à jour de la photo (modifiée) dans le canevas
    global item, Canevas, Mafenetre, photo
    Canevas.delete(ALL)
    photo = PhotoImage(file="image.png")
    #Canevas.itemconfig(item,image=photo)
    item = Canevas.create_image(0,0,anchor=NW, image=photo)
    print("Image de fond (item",item,")")
    Canevas.pack()
#Ajouter sur le même modèle que ci-dessus les fonctions nécessaires


# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('MonPhotoshop')

# Image de fond qui doit faire 400x400"nimporte quoi"
photo = PhotoImage(file="image.png")


# Création d'un canevas de 400x400 pour ouvrir la photo
Largeur = 400
Hauteur = 400
Canevas = Canvas(Mafenetre,width = Largeur, height =Hauteur)
item = Canevas.create_image(0,0,anchor=NW, image=photo)
print("Image de fond (item",item,")")
Canevas.pack()




# Création des boutons
Bouton0 = Button(Mafenetre, text = 'Open', command = imgOpen )
Bouton0.pack(side = LEFT, padx = 5, pady = 5)

Bouton1 = Button(Mafenetre, text = 'Undo', command = undo )
Bouton1.pack(side = LEFT, padx = 5, pady = 5)

Bouton2 = Button(Mafenetre, text = 'Restart', command = restart )
Bouton2.pack(side = LEFT, padx = 5, pady = 5)

Bouton3 = Button(Mafenetre, text = 'Négatif', command = negatif )
Bouton3.pack(side = LEFT, padx = 5, pady = 5)

Bouton4 = Button(Mafenetre, text = 'Miroir X', command = miroirX)
Bouton4.pack(side = LEFT, padx = 5, pady = 5)

Bouton5 = Button(Mafenetre, text = 'Miroir Y', command = miroirY)
Bouton5.pack(side = LEFT, padx = 5, pady = 5)

Bouton6 = Button(Mafenetre, text = 'Banane', command = banane )
Bouton6.pack(side = LEFT, padx = 5, pady = 5)
def quit_and_save():
    Mafenetre.destroy()
    saveNquit()
Bouton7 = Button(Mafenetre, text='Quitter', command=quit_and_save)
Bouton7.pack(side = LEFT, padx = 5, pady = 5)

# Lancement du gestionnaire d'événements
Mafenetre.mainloop()
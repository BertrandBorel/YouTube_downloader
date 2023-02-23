import tkinter as tk
from pytube import YouTube


# création d'une fenêtre tkinter
root = tk.Tk()
root.title("YouTube Downloader")

# création d'un label 
label = tk.Label(root, text="Entrez l'URL de la vidéo YouTube à télécharger:")

# entrée pour insérer l'url
entry = tk.Entry(root, width=50)


# Afficher un message (réussite/échec)
label2 = tk.Label(root, text="")

# fonction pour télécharger la vidéo
def download():
    try : 
        url = entry.get()  # obtenir l'URL à partir de l'entrée
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        label2.configure(text="Le téléchargement est réussi!", foreground="white", background="green")

    except :
        label2.configure(text="Echec...", foreground="white", background="red")


# bouton pour télécharger la vidéo
button = tk.Button(root, text="Télécharger", command=download)

# placement des éléments
label.pack()
entry.pack()
button.pack()
label2.pack()


# lancement de l'application
root.mainloop()
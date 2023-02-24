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


# fonction pour télécharger au format mp4
def download_mp4():
    try : 
        url = entry.get()  # obtenir l'URL à partir de l'entrée
        yt = YouTube(url)
        streams = yt.streams
        audio_streams = streams.filter(only_audio=True)
        audio = audio_streams.first()
        audio.download()
        label2.configure(text="Le téléchargement est réussi!", foreground="white", background="green")

    except :
        label2.configure(text="Echec...", foreground="white", background="red")



# bouton pour télécharger la vidéo
button = tk.Button(root, text="Télécharger vidéo", command=download)

# bouton pour télécharger le son
button2 = tk.Button(root, text="Télécharger mp4", command=download_mp4)

# placement des éléments
label.pack(pady=5)
entry.pack(pady=5)
button.pack(pady=10)
button2.pack()
label2.pack()


# lancement de l'application
root.mainloop()
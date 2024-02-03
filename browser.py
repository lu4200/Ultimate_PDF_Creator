import tkinter as tk
from tkinter import filedialog

selected_files = []  # Liste pour stocker les chemins des fichiers sélectionnés

def browse_files():
    global selected_files
    file_paths = filedialog.askopenfilenames(title="Sélectionner des fichiers")
    selected_files = list(file_paths)
    print("Fichiers sélectionnés :", selected_files)

# Création de la fenêtre
root = tk.Tk()
root.title("Explorateur de fichiers")

# Bouton "Parcourir"
browse_button = tk.Button(root, text="Parcourir", command=browse_files)
browse_button.pack(pady=20)

# Boucle principale
root.mainloop()

# Affichage de la liste des fichiers sélectionnés à la fin
print("Liste finale des fichiers sélectionnés :", selected_files)

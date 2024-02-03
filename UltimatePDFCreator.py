# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    UltimatePDFCreator.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucas <lucas@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/27 15:15:28 by lucas             #+#    #+#              #
#    Updated: 2024/02/03 13:54:36 by lucas            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import PyPDF2
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import os

selected_files = []

def create_pdf(selected_files, margin_bottom):
    with open('NewPDF.pdf', 'wb') as pdf_file:
        pdf_writer = PyPDF2.PdfWriter()

        for image_path in selected_files:
            img = Image.open(image_path)

            # Créer une nouvelle image avec une marge en bas de l'image d'origine
            new_img = Image.new('RGB', (img.width, img.height + margin_bottom), (255, 255, 255))
            new_img.paste(img, (0, 0))

            new_img.save('temp.pdf', 'PDF', resolution=100.0)
            pdf_reader = PyPDF2.PdfReader('temp.pdf')
            page = pdf_reader.pages[0]

            # Ajouter une marge en bas de chaque image
            page.cropbox.left = (page.cropbox.left, page.cropbox.left - margin_bottom)
            pdf_writer.add_page(page)

        pdf_writer.write(pdf_file)

    print("Le fichier PDF a été créé avec succès.")
    os.remove('temp.pdf')
    selected_files = []
    root.destroy()

def browse_files():
    global selected_files
    file_paths = filedialog.askopenfilenames(title="Sélectionner des fichiers")
    selected_files = list(file_paths)
    print("Fichiers sélectionnés :", selected_files)

root = tk.Tk()
root.title("Créateur de PDF")

# Vertical window

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{int(screen_width/4)}x{int(screen_height)}")

# Margin label & entry

margin_label = tk.Label(root, text="Marge en bas de chaque image (en pixels):")
margin_label.pack(pady=10)

margin_var = tk.IntVar()
margin_entry = tk.Entry(root, textvariable=margin_var, width=10)
margin_entry.pack(pady=10)

# Entry for image paths

label = tk.Label(root, text="Sélectionner les images:")
label.pack(pady=10)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=50, state="disabled")
entry.pack(pady=10)

# Browse Button

browse_button = tk.Button(root, text="Parcourir", command=browse_files)
browse_button.pack(pady=10)

# Final button

create_button = tk.Button(root, text="Créer PDF", command=lambda: create_pdf(selected_files, margin_var.get()))
create_button.pack(pady=20)

root.mainloop()













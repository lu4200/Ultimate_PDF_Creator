# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    UltimatePDFCreator.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucas <lucas@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/27 15:15:28 by lucas             #+#    #+#              #
#    Updated: 2024/02/03 13:18:15 by lucas            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import PyPDF2
from PIL import Image
import tkinter as tk
import os

def create_pdf(images, margin_bottom):
    with open('NewPDF.pdf', 'wb') as pdf_file:
        pdf_writer = PyPDF2.PdfWriter()

        for image in images:
            img = Image.open(image)

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
    root.destroy()

root = tk.Tk()
root.title("Créateur de PDF")

# vertical window

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{int(screen_width/4)}x{int(screen_height)}")

# label & entry merging

margin_label = tk.Label(root, text="Marge en bas de chaque image (en pixels):")
margin_label.pack(pady=10)

margin_var = tk.IntVar()
margin_entry = tk.Entry(root, textvariable=margin_var, width=10)
margin_entry.pack(pady=10)

# label & entry IMGs

label = tk.Label(root, text="Noms des images (séparés par des espaces):")
label.pack(pady=10)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=50)
entry.pack(pady=10)

# input handler

def process_input():
    images = entry_var.get().split()
    margin_bottom = margin_var.get()
    create_pdf(images, margin_bottom)

#creation button

create_button = tk.Button(root, text="Créer PDF", command=process_input)
create_button.pack(pady=20)

root.mainloop()












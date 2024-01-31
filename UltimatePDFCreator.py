# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    UltimatePDFCreator.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lumaret <lumaret@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/27 15:15:28 by lucas             #+#    #+#              #
#    Updated: 2024/01/31 18:35:09 by lumaret          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import PyPDF2
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def create_pdf(images):
    with open('NewPDF.pdf', 'wb') as pdf_file:
        pdf_writer = PyPDF2.PdfWriter()

        for image in images:
            img = Image.open(image)
            img.save('temp.pdf', 'PDF', resolution=100.0)
            pdf_reader = PyPDF2.PdfReader('temp.pdf')
            pdf_writer.add_page(pdf_reader.pages[0])

        pdf_writer.write(pdf_file)

    print("Le fichier PDF a été créé avec succès.")
    os.remove('temp.pdf')
    root.destroy()

root = tk.Tk()
root.title("Créateur de PDF")

# label et entry pour entree les noms des images
label = tk.Label(root, text="Noms des images (séparés par des espaces):")
label.pack(pady=10)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=50)
entry.pack(pady=10)

def process_input():
    images = entry_var.get().split()
    create_pdf(images)


create_button = tk.Button(root, text="Créer PDF", command=process_input)
create_button.pack(pady=20)

root.mainloop()



# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    UltimatePDFCreator.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lucas <lucas@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/01/27 15:15:28 by lucas             #+#    #+#              #
#    Updated: 2024/02/03 15:03:20 by lucas            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import PyPDF2
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedTk
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
    root.destroy()

def browse_files():
    global selected_files
    file_paths = filedialog.askopenfilenames(title="Sélectionner des fichiers")
    selected_files = list(file_paths)
    print("Fichiers sélectionnés :", selected_files)

def update_margin_label(value):
    rounded_value = round(value)
    margin_label_var.set(f"Marge en bas de chaque image : {int(rounded_value)} pixels")
    
root = root = ThemedTk(theme="breeze")
root.title("Créateur de PDF")

# Vertical window

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{int(screen_width/4)}x{int(screen_height)}")

# Scrollbar for margin selection
#step_size = 20
margin_var = tk.IntVar()

#def on_scale_arrow_key(event):
#    current_value = margin_var.get()
#    step_size = 10  # Set the step size to 10 or your desired value
#    if event.keysym == 'Right':
#        new_value = min(current_value + step_size, margin_scale['to'])
#    elif event.keysym == 'Left':
#        new_value = max(current_value - step_size, margin_scale['from'])
#   else:
#        return
margin_var.set(new_value)
update_margin_label(new_value)


margin_scale = ttk.Scale(root, from_=0, to=500, orient=tk.HORIZONTAL, length=200, variable=margin_var,
                         style="Horizontal.TScale", command=lambda value: update_margin_label(round(float(value))))

margin_scale.pack(pady=10)

margin_label_var = tk.StringVar()
margin_label = tk.Label(root, textvariable=margin_label_var)
margin_label.pack(pady=10)

margin_var.trace_add("write", lambda *args: update_margin_label(margin_var.get()))


# label for image paths

label = tk.Label(root, text="Sélectionner les images:")
label.pack(pady=10)

# browse button

browse_button = tk.Button(root, text="Parcourir", command=browse_files)
browse_button.pack(pady=10)

# Final button
create_button = tk.Button(root, text="Créer PDF", command=lambda: create_pdf(selected_files, margin_var.get()))
create_button.pack(pady=20)

root.mainloop()















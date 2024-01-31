import PyPDF2
from PIL import Image


image_input = input("Entrez les noms des images séparés par un espace: ")
images = image_input.split()

if len(images) < 2:
    print("Veuillez entrer au moins deux noms d'images.")
    exit()

with open('NewPDF.pdf', 'wb') as pdf_file:
    pdf_writer = PyPDF2.PdfWriter()

    for image in images:
        img = Image.open(image)
        img.save('temp.pdf', 'PDF', resolution=100.0)
        pdf_reader = PyPDF2.PdfReader('temp.pdf')
        pdf_writer.add_page(pdf_reader.pages[0])

    pdf_writer.write(pdf_file)

print("Le fichier PDF a été créé avec succès.")



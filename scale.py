import PyPDF2
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedTk


def on_scale_arrow_key(event):
    current_value = margin_var.get()
    step_size = 10
    if event.keysym == 'Right':
        new_value = min(current_value + step_size, margin_scale['to'])
    elif event.keysym == 'Left':
        new_value = max(current_value - step_size, margin_scale['from'])
    else:
        return
    margin_var.set(new_value)
    update_margin_label(new_value)

def update_margin_label(value):
    margin_label_var.set(f"Marge en bas de chaque image : {int(value)} pixels")

# Create the main window
root = tk.Tk()
root.title("Tkinter Window with Scale Bar")

# Create a scale bar
margin_var = tk.DoubleVar()
margin_scale = ttk.Scale(root, from_=0, to=500, orient=tk.HORIZONTAL, length=200, variable=margin_var,
                         style="Horizontal.TScale")
margin_scale.bind('<Left>', on_scale_arrow_key)
margin_scale.bind('<Right>', on_scale_arrow_key)

# Create a label for displaying the value
margin_label_var = tk.StringVar()
margin_label = tk.Label(root, textvariable=margin_label_var)

# Pack the widgets
margin_scale.pack(pady=10)
margin_label.pack(pady=10)

# Set the initial value
margin_var.set(0)
update_margin_label(0)

root.mainloop()

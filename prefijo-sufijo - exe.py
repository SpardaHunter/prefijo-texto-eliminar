import os
import re
import tkinter as tk
from tkinter import ttk, filedialog

def agregar_prefijo(carpeta, prefijo):
    archivos = os.listdir(carpeta)
    for archivo in archivos:
        nuevo_nombre = prefijo + archivo
        viejo_path = os.path.join(carpeta, archivo)
        nuevo_path = os.path.join(carpeta, nuevo_nombre)
        os.rename(viejo_path, nuevo_path)
        print(f'Renombrado: {archivo} -> {nuevo_nombre}')

def eliminar_sufijo(carpeta, sufijo):
    archivos = os.listdir(carpeta)
    for archivo in archivos:
        nuevo_nombre = re.sub(re.escape(sufijo), '', archivo)
        viejo_path = os.path.join(carpeta, archivo)
        nuevo_path = os.path.join(carpeta, nuevo_nombre)
        os.rename(viejo_path, nuevo_path)
        print(f'Renombrado: {archivo} -> {nuevo_nombre}')

def eliminar_archivos(carpeta, texto_a_eliminar):
    archivos = os.listdir(carpeta)
    for archivo in archivos:
        if texto_a_eliminar in archivo:
            path_a_eliminar = os.path.join(carpeta, archivo)
            os.remove(path_a_eliminar)
            print(f'Eliminado: {archivo}')

def on_option_selected(event):
    selected_option = option_var.get()

    if selected_option == 'AÑADIR PREFIJO':
        prefijo_entry_widget['state'] = 'normal'
        sufijo_entry_widget['state'] = 'disabled'
        eliminar_texto_entry_widget['state'] = 'disabled'
    elif selected_option == 'ELIMINAR TEXTO':
        sufijo_entry_widget['state'] = 'normal'
        prefijo_entry_widget['state'] = 'disabled'
        eliminar_texto_entry_widget['state'] = 'disabled'
    elif selected_option == 'ELIMINAR ARCHIVOS':
        eliminar_texto_entry_widget['state'] = 'normal'
        prefijo_entry_widget['state'] = 'disabled'
        sufijo_entry_widget['state'] = 'disabled'

def execute_operation():
    selected_option = option_var.get()
    selected_folder_path = selected_folder.get()

    if selected_option == 'AÑADIR PREFIJO':
        prefijo = prefijo_entry.get()
        agregar_prefijo(selected_folder_path, prefijo)
    elif selected_option == 'ELIMINAR TEXTO':
        sufijo = sufijo_entry.get()
        eliminar_sufijo(selected_folder_path, sufijo)
    elif selected_option == 'ELIMINAR ARCHIVOS':
        texto_a_eliminar = eliminar_texto_entry.get()
        eliminar_archivos(selected_folder_path, texto_a_eliminar)
    else:
        print(f"Opción no válida. Debes seleccionar '{selected_option}'.")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    selected_folder.set(folder_selected)

# GUI setup
root = tk.Tk()
root.title("PREFIJO-TEXTO-ELIMINAR")

# Folder path
selected_folder = tk.StringVar()

# Options
options = ['AÑADIR PREFIJO', 'ELIMINAR TEXTO', 'ELIMINAR ARCHIVOS']
option_var = tk.StringVar()
option_var.set(options[0])

option_label = tk.Label(root, text="Selecciona una opción:")
option_menu = ttk.Combobox(root, textvariable=option_var, values=options)
option_menu.bind("<<ComboboxSelected>>", on_option_selected)

# Entry widgets
prefijo_label = tk.Label(root, text="Añadir prefijo:")
prefijo_entry = tk.StringVar()
prefijo_entry_widget = tk.Entry(root, textvariable=prefijo_entry, state='normal')

sufijo_label = tk.Label(root, text="Eliminar texto:")
sufijo_entry = tk.StringVar()
sufijo_entry_widget = tk.Entry(root, textvariable=sufijo_entry, state='disabled')

eliminar_texto_label = tk.Label(root, text="Escribe texto para eliminar archivos:")
eliminar_texto_entry = tk.StringVar()
eliminar_texto_entry_widget = tk.Entry(root, textvariable=eliminar_texto_entry, state='disabled')

# Button widgets
select_folder_button = tk.Button(root, text="Seleccionar Carpeta", command=browse_folder)
execute_button = tk.Button(root, text="Ejecutar", command=execute_operation)

# Layout
option_label.grid(row=0, column=0, padx=10, pady=10)
option_menu.grid(row=0, column=1, padx=10, pady=10)
select_folder_button.grid(row=0, column=2, padx=10, pady=10)
prefijo_label.grid(row=1, column=0, padx=10, pady=10)
prefijo_entry_widget.grid(row=1, column=1, padx=10, pady=10)
sufijo_label.grid(row=2, column=0, padx=10, pady=10)
sufijo_entry_widget.grid(row=2, column=1, padx=10, pady=10)
eliminar_texto_label.grid(row=3, column=0, padx=10, pady=10)
eliminar_texto_entry_widget.grid(row=3, column=1, padx=10, pady=10)
execute_button.grid(row=4, column=0, columnspan=3, pady=10)

# Start the GUI
root.mainloop()

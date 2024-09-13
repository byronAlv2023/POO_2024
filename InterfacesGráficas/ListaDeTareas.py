import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Lista para almacenar las tareas
tareas = []

# Función para agregar tarea
def agregar_tarea():
    tarea = entrada.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        tareas.append(tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

# Función para eliminar tarea seleccionada
def eliminar_tarea():
    try:
        tarea_index = lista_tareas.curselection()[0]
        lista_tareas.delete(tarea_index)
        tareas.pop(tarea_index)
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para eliminar.")

# Función para marcar tarea como completada
def completar_tarea():
    try:
        tarea_index = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(tarea_index)
        lista_tareas.delete(tarea_index)
        lista_tareas.insert(tk.END, f"{tarea} - Completado")
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para marcar como completada.")

# Etiqueta
etiqueta = tk.Label(root, text="Tareas pendientes")
etiqueta.pack()

# Campo de texto para ingresar tareas
entrada = tk.Entry(root, width=40)
entrada.pack()

# Botón para agregar tarea
boton_agregar = tk.Button(root, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack()

# Lista de tareas
lista_tareas = tk.Listbox(root, height=10, width=50)
lista_tareas.pack()

# Botón para eliminar tarea
boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack()

# Botón para completar tarea
boton_completar = tk.Button(root, text="Completar Tarea", command=completar_tarea)
boton_completar.pack()

# Iniciar la interfaz
root.mainloop()

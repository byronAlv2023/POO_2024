import tkinter as tk
from tkinter import messagebox, simpledialog

# Función para añadir una nueva tarea a la lista
def add_task(event=None):
    task = entry.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Vacía", "Debes escribir una tarea antes de añadirla.")

# Función para marcar una tarea como completada (doble clic o botón)
def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        # Se marca como completada visualmente añadiendo el prefijo [✔]
        if not task.startswith("[✔]"):
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, "[✔] " + task)
    except IndexError:
        messagebox.showwarning("Error", "Por favor selecciona una tarea.")

# Función para eliminar una tarea de la lista
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Error", "Por favor selecciona una tarea para eliminarla.")

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas de Byron Alvarado")

# Crear el campo de entrada para nuevas tareas
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<Return>", add_task)  # Permitir añadir tarea con la tecla Enter

# Crear el Listbox para mostrar las tareas
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

# Manejador de eventos para doble clic en una tarea
listbox_tasks.bind("<Double-1>", lambda x: complete_task())

# Botón para añadir una nueva tarea
btn_add_task = tk.Button(root, text="Añadir Tarea", width=30, command=add_task)
btn_add_task.pack(pady=5)

# Botón para marcar una tarea como completada
btn_complete_task = tk.Button(root, text="Marcar como Completada", width=30, command=complete_task)
btn_complete_task.pack(pady=5)

# Botón para eliminar una tarea
btn_delete_task = tk.Button(root, text="Eliminar Tarea", width=30, command=delete_task)
btn_delete_task.pack(pady=5)

# Iniciar el bucle de la interfaz gráfica
root.mainloop()

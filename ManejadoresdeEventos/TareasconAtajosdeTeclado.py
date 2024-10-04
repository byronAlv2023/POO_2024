import tkinter as tk
from tkinter import messagebox, Listbox, END, StringVar

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Tareas de Byron Alvarado")

        # Variable para almacenar la tarea nueva
        self.task_var = StringVar()

        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(root, textvariable=self.task_var, width=40)
        self.entry.pack(pady=10)

        # Botón para añadir tareas
        self.add_button = tk.Button(root, text="Añadir Tarea o pulsar > Enter <", command=self.add_task)
        self.add_button.pack(pady=5)

        # Listbox para mostrar las tareas
        self.task_listbox = Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Botones para marcar como completadas y eliminar tareas
        self.complete_button = tk.Button(root, text="Marcar como Completada o pulse la letra > c <", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea o pulse la letra > d <", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Asignar atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())  # Añadir tarea con Enter
        self.root.bind('<c>', lambda event: self.complete_task())  # Marcar como completada con 'C'
        self.root.bind('<d>', lambda event: self.delete_task())  # Eliminar tarea con 'd'
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Cerrar la aplicación con Escape

    def add_task(self):
        """Añadir una nueva tarea a la lista."""
        task = self.task_var.get()
        if task:  # Asegurarse de que la entrada no esté vacía
            self.task_listbox.insert(END, task)  # Añadir tarea a la lista
            self.task_var.set('')  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def complete_task(self):
        """Marcar la tarea seleccionada como completada."""
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener índice de tarea seleccionada
            task = self.task_listbox.get(selected_index)  # Obtener tarea
            self.task_listbox.delete(selected_index)  # Eliminar tarea de la lista
            self.task_listbox.insert(selected_index, task + " (Completada)")  # Añadir tarea completada
            self.task_listbox.itemconfig(selected_index, {'fg': 'green'})  # Cambiar color a verde
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        """Eliminar la tarea seleccionada."""
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener índice de tarea seleccionada
            self.task_listbox.delete(selected_index)  # Eliminar tarea
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()  # Iniciar el bucle principal de la aplicación
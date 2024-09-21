import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        # Inicializa la ventana principal
        self.root = root
        self.root.title("Agenda Personal de Byron Alvarado")

        # Frame para la lista de eventos
        self.frame_list = tk.Frame(self.root)
        self.frame_list.pack(pady=5)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.frame_list, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para entrada de datos
        self.frame_input = tk.Frame(self.root)
        self.frame_input.pack(pady=10)

        # Campos de entrada
        tk.Label(self.frame_input, text="Fecha:").grid(row=0, column=0)
        self.date_entry = DateEntry(self.frame_input, width=12, background='darkblue', foreground='white',
                                    borderwidth=2)
        self.date_entry.grid(row=0, column=1)

        tk.Label(self.frame_input, text="Hora:").grid(row=0, column=2)
        self.hour_entry = tk.Entry(self.frame_input)
        self.hour_entry.grid(row=0, column=3)

        tk.Label(self.frame_input, text="Descripción:").grid(row=1, column=0)
        self.desc_entry = tk.Entry(self.frame_input)
        self.desc_entry.grid(row=1, column=1, columnspan=3)

        # Botones para agregar y eliminar eventos
        self.add_button = tk.Button(self.frame_input, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=2, column=0, pady=10)

        self.delete_button = tk.Button(self.frame_input, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.delete_button.grid(row=2, column=1, pady=10)

        self.exit_button = tk.Button(self.frame_input, text="Salir", command=self.root.quit)
        self.exit_button.grid(row=2, column=2, pady=10)

    def add_event(self):
        """Agregar un nuevo evento a la lista."""
        date = self.date_entry.get()  # Obtiene la fecha ingresada
        hour = self.hour_entry.get()  # Obtiene la hora ingresada
        description = self.desc_entry.get()  # Obtiene la descripción ingresada

        # Verifica que todos los campos estén llenos
        if date and hour and description:
            self.tree.insert("", "end", values=(date, hour, description))  # Agrega el evento al TreeView
            self.clear_entries()  # Limpia los campos de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")  # Mensaje de advertencia

    def delete_event(self):
        """Eliminar el evento seleccionado."""
        selected_item = self.tree.selection()  # Obtiene el evento seleccionado
        if selected_item:
            confirm = messagebox.askyesno("Confirmar",
                                          "¿Estás seguro de que deseas eliminar este evento?")  # Confirmación
            if confirm:
                self.tree.delete(selected_item)  # Elimina el evento
        else:
            messagebox.showwarning("Advertencia",
                                   "Por favor selecciona un evento para eliminar.")  # Mensaje de advertencia

    def clear_entries(self):
        """Limpiar los campos de entrada."""
        self.date_entry.set_date('')  # Reinicia el campo de fecha
        self.hour_entry.delete(0, tk.END)  # Limpia el campo de hora
        self.desc_entry.delete(0, tk.END)  # Limpia el campo de descripción


if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = AgendaApp(root)  # Inicializa la aplicación
    root.mainloop()  # Inicia el bucle de tkinder
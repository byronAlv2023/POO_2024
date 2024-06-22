class Libro:
    def __init__(self, título, autor, disponible):
        self.título = título
        self.autor = autor
        self.disponible = disponible

    def reservar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro {self.título} reservado.")
        else:
            print(f"Libro {self.título} no disponible.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Libro {self.título} devuelto.")
        else:
            print(f"Libro {self.título} no reservado.")

class Reserva:
    def __init__(self, libro, fecha_inicio, fecha_fin):
        self.libro = libro
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def realizar_reserva(self):
        self.libro.reservar()

    def cancelar_reserva(self):
        self.libro.devolver()

# Crear objetos de libro
libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", True)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", True)

# Crear objeto de reserva
reserva1 = Reserva(libro1, "2024-06-20", "2024-06-23")

# Realizar reserva
reserva1.realizar_reserva()

# Cancelar reserva
reserva1.cancelar_reserva()
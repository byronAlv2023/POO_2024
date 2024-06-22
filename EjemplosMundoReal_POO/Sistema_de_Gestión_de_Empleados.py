class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.estado = "activo"

    def asignar_cargo(self, cargo):
        if self.estado == "activo":
            self.estado = "asignado"
            print(f"Empleado {self.nombre} asignado a cargo de {self.cargo}.")
        else:
            print(f"Empleado {self.nombre} no activo.")

class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre

    def realizar(self):
        print(f"Tarea {self.nombre} realizada.")

# Crear objetos de empleado
empleado1 = Empleado("Byron Alvarado", "Gerente")

# Crear objeto de tarea
tarea1 = Tarea("Reporte de ventas")

# Asignar tarea
empleado1.asignar_cargo(tarea1)

# Realizar tarea
tarea1.realizar()
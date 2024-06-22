class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        self.estado = "activo"

    def inscribir_carrera(self, carrera):
        if self.estado == "activo":
            self.estado = "inscrito"
            print(f"Estudiante {self.nombre} inscrito a carrera {self.carrera}.")
        else:
            print(f"Estudiante {self.nombre} no activo.")

class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre

    def realizar(self):
        print(f"Asignatura {self.nombre} realizada.")

# Crear objetos de estudiante
estudiante1 = Estudiante("Byron Alvarado", "Ing.Tecnologias de la informacion")

# Crear objeto de asignatura
asignatura1 = Asignatura("Programacion Orientada a Objetos(POO)")

# Inscribir asignatura
estudiante1.inscribir_carrera(asignatura1)

# Realizar asignatura
asignatura1.realizar()
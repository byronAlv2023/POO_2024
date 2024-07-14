class Mascota:
    # El constructor __init__ inicializa los atributos del objeto Mascota
    # Cuando se crea una nueva instancia de la clase Mascota, este método se ejecuta automáticamente
    def __init__(self, nombre, especie,):
        self.nombre = nombre
        self.especie = especie
        print(f"Se ha creado una nueva mascota: {self.nombre}, {self.especie}")

    # El destructor __del__ se encarga de realizar tareas de limpieza o cierre de recursos
    # Este método se ejecuta automáticamente cuando el objeto Mascota es eliminado
    def __del__(self):
        print(f"La mascota {self.nombre} ha fallecido.")
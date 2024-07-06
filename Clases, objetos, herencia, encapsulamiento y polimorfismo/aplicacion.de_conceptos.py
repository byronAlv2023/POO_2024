"""En este programa, tenemos la clase base Vehiculo que define los atributos y
métodos comunes a cualquier vehículo.La clase derivada Motocicleta hereda de Vehiculo.
La encapsulación se implementa en la clase Vehiculo al utilizar atributos privados
(_marca, _modelo, _año, _velocidad_actual) que solo pueden ser accedidos y
modificados a través de los métodos de la clase.
El polimorfismo se demuestra en el método mostrar_info(), que es sobrescrito en
la clase Motocicleta para incluir información adicional sobre el número de pasajeros.
Se crean instancias de Vehiculo y Motocicleta, y se utilizan sus métodos para
demostrar la funcionalidad del programa."""
#creamos una clase
class Vehiculo:
    """
    Clase base que representa un vehículo.
    """

    def __init__(self, Tipo, modelo, año):
        self._tipo = Tipo  # Atributo encapsulado
        self._modelo = modelo  # Atributo encapsulado
        self._año = año  # Atributo encapsulado
        self._velocidad_actual = 0  # Atributo encapsulado

    def acelerar(self, velocidad):
        """
        Aumenta la velocidad del vehículo.
        """
        self._velocidad_actual += velocidad
        print(f"La {self._tipo} {self._modelo} ahora va a {self._velocidad_actual} km/h.")

    def frenar(self, velocidad):
        """
        Disminuye la velocidad del vehículo.
        """
        self._velocidad_actual -= velocidad
        if self._velocidad_actual < 0:
            self._velocidad_actual = 0
        print(f"La {self._tipo} {self._modelo} ahora va a {self._velocidad_actual} km/h.")

    def mostrar_info(self):
        """
        Muestra la información del vehículo.
        """
        print(f"Tipo: {self._tipo}")
        print(f"Modelo: {self._modelo}")
        print(f"Año: {self._año}")
        print(f"Velocidad actual: {self._velocidad_actual} km/h")


class Motocicleta(Vehiculo):  # Herencia de la clase Vehiculo
    """
    Clase derivada que representa una motocicleta.
    """

    def __init__(self, tipo, modelo, año, num_pasajeros):
        super().__init__(tipo, modelo, año)  # llamamos al constructor init
        self._num_pasajeros = num_pasajeros

    def mostrar_info(self):  # Aplicamos el polimorfismo
        """
        Muestra la información de la motocicleta.
        """
        super().mostrar_info()
        print(f"Número de pasajeros: {self._num_pasajeros}")


# Creamos instancia de Vehículo
vehiculo = Vehiculo("Motocicleta Deportiva", "Honda", 2024)
vehiculo.mostrar_info()
vehiculo.acelerar(50)
vehiculo.frenar(30)

# Creamos instancia de la Motocicleta
Moto = Motocicleta("Motocicleta Todo terreno", "Dukare", 2024, 2)
Moto.mostrar_info()
Moto.acelerar(80)
Moto.frenar(60)
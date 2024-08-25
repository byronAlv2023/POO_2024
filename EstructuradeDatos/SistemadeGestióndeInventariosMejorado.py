# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Constructor para inicializar los atributos del producto
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Método para representar el objeto Producto como una cadena de texto
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        # Constructor para inicializar el inventario con un archivo de almacenamiento
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        # Método para cargar los productos desde un archivo al iniciar el programa
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    id, nombre, cantidad, precio = linea.strip().split(",")
                    self.productos.append(Producto(id, nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            # Excepción si el archivo no existe; se crea un nuevo archivo
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo.")
            open(self.archivo, "w").close()
        except PermissionError:
            # Excepción si no hay permisos para acceder al archivo
            print(f"Permiso denegado para acceder a {self.archivo}.")

    def guardar_inventario(self):
        # Método para guardar los productos en el archivo después de cada modificación
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
        except PermissionError:
            # Excepción si no hay permisos para escribir en el archivo
            print(f"Permiso denegado para escribir en {self.archivo}.")

    def añadir_producto(self, producto):
        # Método para añadir un nuevo producto al inventario
        if any(p.id == producto.id for p in self.productos):
            # Verifica si el ID del producto ya existe
            print("ID de producto duplicado. No se puede añadir.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id):
        # Método para eliminar un producto del inventario por su ID
        producto_a_eliminar = next((p for p in self.productos if p.id == id), None)
        if producto_a_eliminar:
            self.productos.remove(producto_a_eliminar)
            self.guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        # Método para actualizar la cantidad o el precio de un producto por su ID
        producto = next((p for p in self.productos if p.id == id), None)
        if producto:
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            self.guardar_inventario()
            print("Producto actualizado exitosamente.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Método para buscar productos por nombre
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print("No se encontraron productos.")

    def mostrar_todos(self):
        # Método para mostrar todos los productos en el inventario
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("Inventario vacío.")

# Interfaz de Usuario en la Consola
def menu():
    # Función para mostrar el menú interactivo al usuario
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Añadir un nuevo producto
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            inventario.añadir_producto(Producto(id, nombre, cantidad, precio))
        elif opcion == "2":
            # Eliminar un producto
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            # Actualizar un producto
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "4":
            # Buscar un producto
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            # Mostrar todos los productos
            inventario.mostrar_todos()
        elif opcion == "6":
            # Salir del programa
            break
        else:
            # Opción no válida
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

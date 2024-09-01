class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado del inventario.")
        else:
            print(f"No se encontró ningún producto con ID {id_producto}.")

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].set_cantidad(nueva_cantidad)
            print(f"Cantidad actualizada para el producto con ID {id_producto}.")
        else:
            print(f"No se encontró ningún producto con ID {id_producto}.")

    def actualizar_precio(self, id_producto, nuevo_precio):
        if id_producto in self.productos:
            self.productos[id_producto].set_precio(nuevo_precio)
            print(f"Precio actualizado para el producto con ID {id_producto}.")
        else:
            print(f"No se encontró ningún producto con ID {id_producto}.")

    def buscar_producto(self, nombre):
        productos_encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                productos_encontrados.append(producto)
        return productos_encontrados

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

import pickle

def guardar_inventario(inventario, archivo):
    with open(archivo, 'wb') as f:
        pickle.dump(inventario, f)
    print("Inventario guardado exitosamente.")

def cargar_inventario(archivo):
    try:
        with open(archivo, 'rb') as f:
            inventario = pickle.load(f)
        return inventario
    except FileNotFoundError:
        print("No se encontró el archivo de inventario.")
        return None

def main():
    inventario = Inventario()

    while True:
        print("\nMenú de Gestión de Inventario:")
        print("1. Agregar un nuevo producto")
        print("2. Eliminar un producto")
        print("3. Actualizar la cantidad de un producto")
        print("4. Actualizar el precio de un producto")
        print("5. Buscar productos por nombre")
        print("6. Mostrar todos los productos en el inventario")
        print("7. Guardar el inventario en un archivo")
        print("8. Cargar el inventario desde un archivo")
        print("9. Salir del programa")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            id_producto = int(input("Ingrese el ID del producto: "))
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            precio_producto = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre_producto, cantidad_producto, precio_producto)
            inventario.agregar_producto(producto)
            print("Producto agregado exitosamente al inventario.")

        elif opcion == '2':
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_cantidad(id_producto, nueva_cantidad)

        elif opcion == '4':
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            inventario.actualizar_precio(id_producto, nuevo_precio)

        elif opcion == '5':
            nombre_producto = input("Ingrese el nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_producto(nombre_producto)
            if productos_encontrados:
                print(f"Productos encontrados que contienen '{nombre_producto}':")
                for producto in productos_encontrados:
                    print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
            else:
                print(f"No se encontraron productos que contengan '{nombre_producto}'.")

        elif opcion == '6':
            inventario.mostrar_productos()

        elif opcion == '7':
            archivo_inventario = input("Ingrese el nombre del archivo para guardar el inventario: ")
            guardar_inventario(inventario, archivo_inventario)

        elif opcion == '8':
            archivo_inventario = input("Ingrese el nombre del archivo para cargar el inventario: ")
            inventario_cargado = cargar_inventario(archivo_inventario)
            if inventario_cargado:
                inventario = inventario_cargado
                print("Inventario cargado exitosamente.")

        elif opcion == '9':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 9.")

if __name__ == '__main__':
    main()
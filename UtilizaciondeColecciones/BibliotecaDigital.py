# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.categoria = categoria
        self.isbn = isbn

    # Método para obtener el título y el autor (inmutables)
    def obtener_info(self):
        return (self.__titulo, self.__autor)

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    # Método para añadir libros a la lista de libros prestados
    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    # Método para devolver libros
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    # Mostrar libros prestados
    def mostrar_libros_prestados(self):
        if not self.libros_prestados:
            print(f"El usuario {self.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:
                print(f"- {libro.obtener_info()}")

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario ISBN: Libro
        self.usuarios = set()  # Conjunto de IDs de usuarios

    # Añadir libro a la biblioteca
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.obtener_info()}' añadido a la biblioteca.")

    # Eliminar libro de la biblioteca
    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro '{libro.obtener_info()}' eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn} en la biblioteca.")

    # Registrar usuario en la biblioteca
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado en la biblioteca.")

    # Dar de baja a un usuario
    def eliminar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            self.usuarios.remove(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' eliminado de la biblioteca.")
        else:
            print(f"Usuario con ID {usuario.id_usuario} no está registrado.")

    # Prestar libro a un usuario
    def prestar_libro(self, isbn, usuario):
        if isbn in self.libros:
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.obtener_info()}' prestado a {usuario.nombre}.")
        else:
            print(f"El libro con ISBN {isbn} no está disponible en la biblioteca.")

    # Devolver libro de un usuario
    def devolver_libro(self, isbn, usuario):
        libro = self.libros.get(isbn)
        if libro:
            usuario.devolver_libro(libro)
            print(f"Libro '{libro.obtener_info()}' devuelto por {usuario.nombre}.")
        else:
            print(f"El libro con ISBN {isbn} no pertenece a esta biblioteca.")

    # Buscar libro por título, autor o categoría
    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros.values() if getattr(libro, criterio) == valor]
        if resultados:
            print(f"Libros encontrados bajo {criterio} '{valor}':")
            for libro in resultados:
                print(f"- {libro.obtener_info()}")
        else:
            print(f"No se encontraron libros bajo {criterio} '{valor}'.")

    # Mostrar Todos los libros
    def mostrar_todos_libros(self):
        if self.libros:
            print("Lista de libros en la biblioteca:")
            for libro in self.libros.values():
                print(f"- {libro.obtener_info()}")
        else:
            print("No hay libros en la biblioteca.")

# Función del menú principal
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Sistema de Gestión de Biblioteca Digital ---")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Eliminar usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Mostrar libros prestados por un usuario")
        print("9. Mostrar todos los libros")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == '2':
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == '3':
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '4':
            id_usuario = input("ID del usuario a eliminar: ")
            nombre = input("Nombre del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.eliminar_usuario(usuario)

        elif opcion == '5':
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario: ")
            nombre = input("Nombre del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.prestar_libro(isbn, usuario)

        elif opcion == '6':
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario: ")
            nombre = input("Nombre del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.devolver_libro(isbn, usuario)

        elif opcion == '7':
            criterio = input("Buscar por (titulo/autor/categoria): ")
            valor = input(f"Ingrese el {criterio}: ")
            biblioteca.buscar_libro(criterio, valor)

        elif opcion == '8':
            id_usuario = input("ID del usuario: ")
            nombre = input("Nombre del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            usuario.mostrar_libros_prestados()

        elif opcion == '9':
            biblioteca.mostrar_todos_libros()

        elif opcion == '0':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()

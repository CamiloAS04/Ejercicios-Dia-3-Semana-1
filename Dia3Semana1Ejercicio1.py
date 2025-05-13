#Diccionario inicial
biblioteca = {
    '001' : {'titulo': 'Cien años de soledad', 'autor': 'Gabriel Garcia Marquez', 'año': '1997'},
    '002' : {'titulo': '1984', 'autor': 'George Orwell', 'año': '1949'}
}

#Funcion para agregar un libro
def agregar_libro():
    id_libro = input("ID del libro").strip()
    if id_libro in biblioteca:
        print("Ese ID ya existe. Usa otro")
        return 
    titulo = input("Titulo:").strip()
    autor = input("Autor:").strip()
    try:
        año = int(input("Año de publicacion:").strip())
    except ValueError:
        print("Año invalido")
        return
    biblioteca[id_libro] = {'titulo': titulo,'autor': autor, 'año': año}
    print("Libro Agregado correctamente")

#Funcion para mostrar todos los libros
def mostrar_libro():
    if not biblioteca:
        print("No hay libros en la biblioteca")
        return
    for id_libro, datos in biblioteca.items():
        print(f"ID: {id_libro} | Titulo: {datos['titulo']} | Autor: {datos['autor']} | Año{datos['año']}")

#Funcion para buscar libros por ID o nombre
def buscar_libros():
    criterio = input("Buscar por ID o titulo:").strip().lower()
    encontrado = False
    for id_libro, datos in biblioteca.items():
        if criterio == id_libro.lower() or criterio == datos['titulo'].lower():
            print(f"ID: {id_libro} | Titulo: {datos['titulo']} | Autor: {datos['autor']} | Año{datos['año']}")
            encontrado = True
        if not encontrado:
            print("Libro no encontrado")

#Funcion para actualizar libro por ID o nombre
def actualizar_libro():
    id_libro = input("ID del libro que desead actualizar:").strip()
    if id_libro not in biblioteca:
        print("Ese ID no existe")
        return
    print ("Deja vacio lo que no deseas cambiar")
    nuevo_titulo = input("Nuevo titulo:").strip()
    nuevo_autor = input("Nuevo autor:").strip()
    nuevo_año = input("Nuevo año:").strip()
    if nuevo_titulo:
        biblioteca[id_libro]['titulo'] = nuevo_titulo
    if nuevo_autor:
        biblioteca[id_libro]['autor'] = nuevo_autor
    if nuevo_año:
        biblioteca[id_libro]['año'] = nuevo_año
        print ("Libro actualizado correctamente")

#Funcion para eliminar libro por ID
def eliminar_libro():
    id_libro = input("ID del libro a eliminar:").strip()
    if id_libro in  biblioteca:
        del biblioteca[id_libro]
        print("Libro eliminado correctamente")
    else:
        print("ID no encontrado")

#Menu principal
def menu():
    while True:
        print("\n--- Gestion de biblioteca ---")
        print("1. Agregar libro")
        print("2. Mostrar todos los libros")
        print("3. Buscar libro")
        print("4. Actualizar libro")
        print("5. Eliminar libro")
        print("6. Salir")
        opcion = input("Elige una opcion (1-6):").strip()

        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            mostrar_libro()
        elif opcion == '3':
            buscar_libros()
        elif opcion == '4':
            actualizar_libro()
        elif opcion == '5':
            eliminar_libro()
        elif opcion == '6':
            print("Hasta luego")
            break
        else:
            print("Opcion no valida")

#Ejecutar programa
menu()
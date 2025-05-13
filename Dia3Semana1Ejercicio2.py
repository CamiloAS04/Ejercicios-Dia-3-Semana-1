#Diccionario para almacenar los contactos
agenda = {}

#Funcion para agregar un nuevo contacto
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto:").strip()
    if nombre in agenda:
        print("Este contacto ya existe")
        return
    telefono = input("Ingrese el numero de telefono:").strip()
    email = input("Ingrese el correo electronico:").strip()
    agenda[nombre] = {"Telefono": telefono, "Email": email}
    print(f"Contacto {nombre} agregado correctamente")

#Funcion para listar contactos
def listar_contactos():
    if not agenda:
        print("La agenda esta vacia")
        return
    print("\nLista de contactos:")
    for nombre, info in agenda.items():
        print(f"- {nombre}: Telefono: {info['telefono']}, Email: {info['email']}")
        print()

#Funcion para buscar un contacto
def buscar_contactos():
    nombre = input("Ingrese nombre del contacto a buscar:").strip()
    if nombre in agenda:
        info = agenda[nombre]
        print(f"contacto encontrado - {nombre}: Telefono: {info['telefono']}, Email: {info['email']}")
    else:
        print("Contacto no encontrado")

#Funcion para actualizar contactos
def actualizar_contacto():
    nombre = input("Ingrese nombre del contacto a actualizar").strip()
    if nombre not in agenda:
        print("El contacto no existe")
        return
    print("¿Que deseas actualizar?")
    print("1. Telefono")
    print("2. Email")
    opcion = input("seleccione una opcion (1 o 2)").strip()
    if opcion == "1":
        nuevo_telefono = input("Ingrese el nuevo numero de telefono:").strip()
        agenda[nombre]["telefono"] = nuevo_telefono
        print("Telefono actualizado correctamente")
    elif opcion == "2":
        nuevo_email = input("Ingrese el nuevo correo electronico:").strip()
        agenda[nombre]["email"] = nuevo_email
        print("Correo electronico actualizado correctamente")
    else:
        print("opcion no valida")

#Funcion para eleminar un contacto
def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea eliminar:").strip()
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado correctamente")
    else:
        print("El contacto no existe")

#Menu principal
def menu():
    while True:
        print("\n--- Agenda de contactos ---")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Actualizar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")
        opcion = input("Elige una opcion (1-6):").strip()

        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            listar_contactos()
        elif opcion == '3':
            buscar_contactos()
        elif opcion == '4':
            actualizar_contacto()
        elif opcion == '5':
            eliminar_contacto()
        elif opcion == '6':
            print("Hasta luego")
            break
        else:
            print("Opcion no valida")

#Ejecutar programa
menu()
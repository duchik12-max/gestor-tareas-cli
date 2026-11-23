tareas = []

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS CLI ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "5":
            print("Saliendo del gestor...")
            break
        else:
            print("Opción no implementada aún.")

if __name__ == "__main__":
    main()

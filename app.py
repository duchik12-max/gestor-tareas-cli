tareas = []

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS CLI ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def completar_tarea():
    idx = int(input("Número de tarea a completar: ")) - 1
    if 0 <= idx < len(tareas):
        tareas[idx]["completada"] = True
        print("Tarea marcada como completada.")

def eliminar_tarea():
    idx = int(input("Número de tarea a eliminar: ")) - 1
    if 0 <= idx < len(tareas):
        tareas.pop(idx)
        print("Tarea eliminada.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Saliendo del gestor...")
            break
        else:
            print("Opción no implementada aún.")

if __name__ == "__main__":
    main()

tareas = []

def mostrar_menu():
    print("\n=== GESTOR DE TAREAS CLI v1.0 ===")
    print("Ayuda: Ingrese el numero de la accion deseada.")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def agregar_tarea():
    titulo = input("Ingrese el titulo de la tarea: ").strip()
    if not titulo:
        print("Error: El titulo de la tarea no puede estar vacio.")
        return
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada con exito.")

def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    for i, t in enumerate(tareas,1):
        estado = "✔" if t["completada"] else "✘"
        print(f"{i}. [{estado}] {t['titulo']}")

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
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        if opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Saliendo del gestor...")
            break
        else:
            print("Opción invalida.")

if __name__ == "__main__":
    main()

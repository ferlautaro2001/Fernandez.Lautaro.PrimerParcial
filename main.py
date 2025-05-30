from registro import registrar_usuario, registrar_empresa, registrar_cantidad, detallar_transacciones
from consultas import visualizar, ejecutar_submenu_consultas
from utilidades import reconocer_numero

def main() -> None:
    nombres_transacciones = []
    acciones_transacciones = []
    cantidades_transacciones = [] 
    datos_cargados = False
    continuar_programa = True

    while continuar_programa:
        print("\n--- MENÚ UTN-Capital ---")
        print("1. Registrar Transacción")
        print("2. Visualizar todos los datos")
        print("3. Consultas")
        print("4. Salir")
        opcion_str = input("Opción: ")
        es_opcion_valida_formato = True
        if not opcion_str: 
            es_opcion_valida_formato = False
        else:
            for i in range(len(opcion_str)):
                if not reconocer_numero(opcion_str[i]):
                    es_opcion_valida_formato = False
                    break

        if not es_opcion_valida_formato:
            print("Error: Opción inválida, ingrese un número.")
            input("\nPresione Enter para continuar...")
            continue
        
        opcion = int(opcion_str)

        if opcion == 1:
            usuario = registrar_usuario()
            accion = registrar_empresa()
            cantidad = registrar_cantidad()
            if (usuario and accion and cantidad):
                nombres_transacciones += [usuario]    
                acciones_transacciones += [accion]      
                cantidades_transacciones += [cantidad] 
                datos_cargados = True
                print("\n--- ¡Transacción guardada en las listas correspondientes! ---")
        elif opcion == 2:
            if datos_cargados:
                transacciones = detallar_transacciones(nombres_transacciones,acciones_transacciones,cantidades_transacciones)
                visualizar(transacciones)
            else:
                print("⚠️ Primero debe registrar transacciones (opción 1).")
        elif opcion == 3:
            if datos_cargados:
                ejecutar_submenu_consultas(
                    nombres_transacciones,
                    acciones_transacciones,
                    cantidades_transacciones
                )
            else:
                print("⚠️ Primero debe registrar transacciones (opción 1).")
        elif opcion == 4:
            print("Saliendo del programa...")
            continuar_programa = False
        else:
            print("Opción no válida.")

        if continuar_programa:
            input("\nPresione Enter para continuar...")

    return None

if __name__ == "__main__":
    main()

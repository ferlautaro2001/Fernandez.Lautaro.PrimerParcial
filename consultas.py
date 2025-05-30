from utilidades import ordenar_alfabeticamente, reconocer_numero
from registro import detallar_transacciones
from datos import empresas_normalizadas

def visualizar(registro_transacciones: list) -> None:
    """
    Muestra un listado de transacciones ordenadas alfabéticamente por usuario.

    Args:
        registro_transacciones (list): Lista de transacciones: i[0]=Nombre, i[1]=Empresa, i[2]=Precio, i[3]= Cantidad, i[4]= Total invertido.
        
    Returns:
        None: Imprime un informe estructurado de las transacciones en la consola.

    Funcionamiento:
    - Si no hay transacciones, muestra un mensaje de advertencia.
    - Crea una copia de la lista de transacciones para evitar modificar la original.
    - Ordena las transacciones alfabéticamente por el nombre del usuario usando `ordenar_alfabeticamente`.
    - Formatea y muestra los datos en una tabla estructurada con alineación adecuada.
    """
    if not registro_transacciones:
        print("\n⚠️ No hay transacciones registradas para mostrar.")
    else:
        copia_array_transacciones = []
        for i in range(len(registro_transacciones)):
            copia_array_transacciones += [registro_transacciones[i][:]]
        ordenar_alfabeticamente(copia_array_transacciones, 0) 
        print("\n--- 🧾 Listado Completo de Transacciones (Ordenado por Usuario A-Z) ---")
        print(f"{'Usuario':<20} {'Acción':<10} {'Precio/U':<12} {'Cantidad':<10} {'Total USD':<12}")
        print("-" * 70)
        for i in range(len(copia_array_transacciones)):
            transaccion = copia_array_transacciones[i]
            usuario = transaccion[0]
            accion = transaccion[1]
            precio_unidad = f"${transaccion[2]:.2f}"
            cantidad_ingresada = f"{transaccion[3]}" 
            total_invertido = f"${transaccion[4]:.2f}"
            print(f"{usuario:<20} {accion:<10} {precio_unidad:<12} {cantidad_ingresada:<10} {total_invertido:<12}")
        print("-" * 70)
    return None

def consultar_total_acciones(registro_transacciones: list) -> None:
    """
    Calcula y muestra la cantidad total de acciones por usuario a partir de un registro de transacciones.

    Args:
        registro_transacciones (list): Lista de transacciones: i[0]=Nombre, i[1]=Empresa, i[2]=Precio, i[3]= Cantidad, i[4]= Total invertido.
        
    Returns:
        None: Imprime la cantidad total de acciones por usuario en la consola.

    Funcionamiento:
    - Se recorre la lista de transacciones y se acumulan las acciones por usuario.
    - Se evita el doble conteo utilizando listas auxiliares (`suma_usuarios` y `nombres_procesados`).
    - Se muestran los resultados en pantalla con el formato adecuado.
    """
    print("\n--- 🔢 Cantidad Total de Acciones por Usuario ---")
    if not registro_transacciones:
        print("No hay datos.")
    else:
        suma_usuarios = []
        nombres_procesados = []
        for i in range(len(registro_transacciones)):
            usuario = registro_transacciones[i][0]
            cantidad = registro_transacciones[i][3]
            esta = False
            for j in range(len(nombres_procesados)):
                if nombres_procesados[j] == usuario:
                    esta = True
                    for i in range(len(suma_usuarios)):
                        if suma_usuarios[i][0] == usuario:
                            suma_usuarios[i][1] += cantidad
                            break
                    break
            if not esta:
                suma_usuarios += [[usuario, cantidad]]
                nombres_procesados += [usuario]
        for i in range(len(suma_usuarios)):
            print(f"👤 {suma_usuarios[i][0]}: {suma_usuarios[i][1]} acciones")
    return None

def consultar_promedio_empresas(registro_transacciones: list) -> None:
    """
    Calcula y muestra el promedio de acciones adquiridas por empresa en base a un registro de transacciones.

    Args:
        registro_transacciones (list): Lista de transacciones: i[0]=Nombre, i[1]=Empresa, i[2]=Precio, i[3]= Cantidad, i[4]= Total invertido.
        
    Returns:
        None: Imprime el promedio de acciones adquiridas por empresa en la consola.

    Funcionamiento:
    - Se extrae el conjunto de usuarios únicos que han participado en transacciones.
    - Se calcula la cantidad total de acciones adquiridas por empresa.
    - Se obtiene el promedio de acciones por empresa dividiendo la cantidad total entre el número de usuarios activos.
    - Si no hay usuarios activos, se ajusta el divisor para evitar errores de división por cero.
    - Se muestra el resultado.
    """
    print("\n--- 📈 Promedio de Acciones Adquiridas por Empresa ---")
    if not registro_transacciones:
        print("No hay datos.")
    else:
        acciones_sumas = [] 
        usuarios_unicos = [] 
        for i in range(len(registro_transacciones)):
            usuario = registro_transacciones[i][0]
            esta = False
            for j in range(len(usuarios_unicos)):
                if usuarios_unicos[j] == usuario:
                    esta = True
                    break
            if not esta:
                usuarios_unicos += [usuario]
        usuarios_activos = len(usuarios_unicos)
        if usuarios_activos == 0:
            usuarios_activos = 1 
        for i in range(len(empresas_normalizadas)):
            accion = empresas_normalizadas[i]
            suma_cantidad_accion = 0
            for j in range(len(registro_transacciones)):
                if registro_transacciones[j][1] == accion:
                    suma_cantidad_accion += registro_transacciones[j][3]
            promedio = suma_cantidad_accion / usuarios_activos
            acciones_sumas += [[accion, promedio]]
        for i in range(len(acciones_sumas)):
            print(f"🏭 {acciones_sumas[i][0]}: {acciones_sumas[i][1]:.2f} acciones en promedio")
    return None

def consultar_usuarios_total(registro_transacciones: list) -> None:
    """
    Calcula y muestra el total invertido por cada usuario en orden alfabético.

    Args:
        registro_transacciones (list): Lista de transacciones: i[0]=Nombre, i[1]=Empresa, i[2]=Precio, i[3]= Cantidad, i[4]= Total invertido.

    Comportamiento:
    - Si `registro_transacciones` está vacío, muestra "No hay datos."
    - Suma el total invertido por cada usuario, asegurando que no se dupliquen nombres.
    - Ordena la lista de usuarios alfabéticamente utilizando `ordenar_alfabeticamente`.
    - Imprime el resultado con cada usuario y su inversión total en USD.

    Retorno:
    None
    """
    print("\n--- 🔃 Usuarios (A-Z) con Total Invertido ---")
    if not registro_transacciones:
        print("No hay datos.")
    else:
        usuarios_inversiones = []
        nombres_procesados = []
        for i in range(len(registro_transacciones)):
            usuario = registro_transacciones[i][0]
            total_invertido_transaccion = registro_transacciones[i][4]
            esta = False
            for j in range(len(nombres_procesados)):
                if nombres_procesados[j] == usuario:
                    esta = True
                    for k in range(len(usuarios_inversiones)):
                        if usuarios_inversiones[k][0] == usuario:
                            usuarios_inversiones[k][1] += total_invertido_transaccion
                            break
                    break
            if not esta:
                usuarios_inversiones += [[usuario, total_invertido_transaccion]]
                nombres_procesados += [usuario]
        ordenar_alfabeticamente(usuarios_inversiones, 0)
        for i in range(len(usuarios_inversiones)):
            print(f"👤 {usuarios_inversiones[i][0]}: ${usuarios_inversiones[i][1]:.2f} USD")
    return None

def consultar_inversion_total(registro_transacciones: list) -> float:
    """
    Calcula el monto total invertido en todas las transacciones registradas.

    Args:
        registro_transacciones (list): Lista de transacciones: i[0]=Nombre, i[1]=Empresa, i[2]=Precio, i[3]= Cantidad, i[4]= Total invertido.

    Comportamiento:
    - Recorre `registro_transacciones` sumando el monto invertido de cada transacción.
    - Devuelve el valor acumulado.

    Retorno:
    - (float): Monto total invertido en la cartera de transacciones.
    """
    inversion_total = 0.0
    for i in range(len(registro_transacciones)):
        inversion_total += registro_transacciones[i][4]
    return inversion_total

def consultar_acciones_usuario(registro_transacciones: list) -> None:
    """
    Identifica la empresa en la que cada usuario ha adquirido la mayor cantidad de acciones y muestra el resultado.

    Args:
        registro_transacciones (list): Lista de transacciones: i[0]=Nombre, i[1]=Empresa, i[2]=Precio, i[3]= Cantidad, i[4]= Total invertido.

    Comportamiento:
    - Si no hay registros en `registro_transacciones`, muestra "No hay datos."
    - Obtiene una lista de usuarios únicos.
    - Calcula la cantidad total de acciones adquiridas por cada usuario, agrupadas por empresa.
    - Determina la empresa con más acciones por usuario y muestra el resultado.

    Retorno:
    None
    """    
    print("\n--- 🥇 Empresa con Mayor Cantidad de Acciones por Usuario ---")
    
    if not registro_transacciones:
        print("No hay datos.")
    else:
        lista_usuarios = []
        for i in range(len(registro_transacciones)):
            usuario_actual = registro_transacciones[i][0]
            existe_usuario = False
            for j in range(len(lista_usuarios)):
                if lista_usuarios[j] == usuario_actual:
                    existe_usuario = True
                    break
            if not existe_usuario:
                lista_usuarios += [usuario_actual]

        for i in range(len(lista_usuarios) - 1):
            for j in range(len(lista_usuarios) - i - 1):
                if lista_usuarios[j] > lista_usuarios[j+1]:
                    lista_usuarios[j], lista_usuarios[j+1] = lista_usuarios[j+1], lista_usuarios[j]
                    
        for i in range(len(lista_usuarios)):
            usuario = lista_usuarios[i]
            acciones_por_empresa = []
            for j in range(len(registro_transacciones)):
                if registro_transacciones[j][0] == usuario:
                    empresa_actual = registro_transacciones[j][1]
                    cantidad_acciones = registro_transacciones[j][3]
                    empresa_existente = False
                    for k in range(len(acciones_por_empresa)):
                        if acciones_por_empresa[k][0] == empresa_actual:
                            acciones_por_empresa[k][1] += cantidad_acciones
                            empresa_existente = True
                            break
                    if not empresa_existente:
                        acciones_por_empresa += [[empresa_actual, cantidad_acciones]]
            
            if not acciones_por_empresa:
                print(f"👤 {usuario}: No tiene acciones registradas.")
                continue
            
            empresa_mayor_acciones = acciones_por_empresa[0][0]
            cantidad_maxima = acciones_por_empresa[0][1]
            for j in range(1, len(acciones_por_empresa)):
                if acciones_por_empresa[j][1] > cantidad_maxima:
                    cantidad_maxima = acciones_por_empresa[j][1]
                    empresa_mayor_acciones = acciones_por_empresa[j][0]
            
            print(f"👤 {usuario}: Más acciones en {empresa_mayor_acciones} ({cantidad_maxima} acciones)")
    
    return None

def consultar_mayor_accion(registro_transacciones: list) -> None:
    """
    Determina qué acción tuvo la mayor inversión total en dólares dentro de la cartera de usuarios.

    Args:
        registro_transacciones (list): Lista de transacciones: i[0]=Nombre, i[1]=Empresa, i[2]=Precio, i[3]= Cantidad, i[4]= Total invertido.

    Comportamiento:
    - Si `registro_transacciones` está vacío, muestra "No hay datos."
    - Calcula la inversión total por cada empresa.
    - Identifica la empresa con el mayor monto de inversión acumulada.
    - Muestra el resultado con el nombre de la acción y el total invertido.

    Retorno:
    None
    """    
    print("\n--- 💰 Acción con Mayor Inversión Total (USD) ---")
    
    if not registro_transacciones:
        print("No hay datos.")
    else:
        inversiones_por_empresa = []
        for i in range(len(empresas_normalizadas)):
            empresa_actual = empresas_normalizadas[i]
            total_invertido_empresa = 0.0
            for j in range(len(registro_transacciones)):
                if registro_transacciones[j][1] == empresa_actual:
                    total_invertido_empresa += registro_transacciones[j][4]
            inversiones_por_empresa += [[empresa_actual, total_invertido_empresa]]

        if not inversiones_por_empresa:
            print("No se pudo calcular la inversión por empresa.")
        else:
            empresa_mayor_inversion = inversiones_por_empresa[0][0]
            monto_mayor_inversion = inversiones_por_empresa[0][1]
            for i in range(1, len(inversiones_por_empresa)):
                if inversiones_por_empresa[i][1] > monto_mayor_inversion:
                    monto_mayor_inversion = inversiones_por_empresa[i][1]
                    empresa_mayor_inversion = inversiones_por_empresa[i][0]

            print(f"🥇 Acción: {empresa_mayor_inversion}, Total Invertido: ${monto_mayor_inversion:.2f} USD")

    return None

def consulta_porcentaje_inversion_por_usuario(registro_transacciones: list) -> None:
    """
    Calcula y muestra el porcentaje de inversión de cada usuario respecto al total de la cartera.

    Args:
        registro_transacciones (list): Lista de transacciones: i[0]=Nombre, i[1]=Empresa, i[2]=Precio, i[3]= Cantidad, i[4]= Total invertido.

    Comportamiento:
    - Si "registro_transacciones" está vacío, muestra "No hay datos."
    - Obtiene la inversión total acumulada de la cartera.
    - Suma la inversión individual de cada usuario.
    - Calcula y muestra el porcentaje que representa cada usuario respecto al total.

    Retorno:
    None
    """    
    print("\n--- 📉 Porcentaje de Inversión por Usuario ---")
    if not registro_transacciones:
        print("No hay datos.")
    else:
        total_cartera = consultar_inversion_total(registro_transacciones)
        if total_cartera == 0:
            print("La inversión total de la cartera es 0, no se puede calcular porcentaje.")
        else:
            usuarios_inversiones = [] 
            nombres_procesados = []
            for i in range(len(registro_transacciones)):
                usuario = registro_transacciones[i][0]
                total_invertido_transaccion = registro_transacciones[i][4]
                esta = False
                for j in range(len(nombres_procesados)):
                    if nombres_procesados[j] == usuario:
                        esta = True
                        for k in range(len(usuarios_inversiones)):
                            if usuarios_inversiones[k][0] == usuario:
                                usuarios_inversiones[k][1] += total_invertido_transaccion
                                break
                        break
                if not esta:
                    usuarios_inversiones += [[usuario, total_invertido_transaccion]]
                    nombres_procesados += [usuario]
            for i in range(len(usuarios_inversiones)):
                porcentaje = (usuarios_inversiones[i][1] / total_cartera) * 100
                print(f"👤 {usuarios_inversiones[i][0]}: {porcentaje:.2f}% del total")
    return None

def consulta_usuarios_superan_promedio_inversion(registro_transacciones: list) -> None:
    """
    Identifica y muestra los usuarios cuya inversión total supera el promedio de inversión.

    Args:
        registro_transacciones (list): Lista de transacciones: i[0]=Nombre, i[1]=Empresa, i[2]=Precio, i[3]= Cantidad, i[4]= Total invertido.

    Comportamiento:
    - Si "registro_transacciones" está vacío, muestra "No hay datos."
    - Obtiene la lista de usuarios únicos con transacciones registradas.
    - Calcula la inversión promedio de todos los usuarios.
    - Recorre los usuarios y verifica quiénes superan la inversión promedio.
    - Muestra el listado de usuarios que cumplen la condición.

    Retorno:
    None
    """
    print("\n--- 💰 Usuarios que Superan la Inversión Promedio ---")
    if not registro_transacciones:
        print("No hay datos.")
    else:
        usuarios_unicos = []
        for i in range(len(registro_transacciones)):
            usuario = registro_transacciones[i][0]
            esta = False
            for j in range(len(usuarios_unicos)):
                if usuarios_unicos[j] == usuario:
                    esta = True
                break
            if not esta: usuarios_unicos += [usuario]
        usuarios_activos = len(usuarios_unicos)
        if usuarios_activos == 0:
            print("No hay usuarios con transacciones para calcular el promedio.")
        else:
            total_cartera = consultar_inversion_total(registro_transacciones)
            promedio_inversion = total_cartera / usuarios_activos
            print(f"(Inversión promedio por usuario: ${promedio_inversion:.2f} USD)")
            usuarios_superan_res = []
            usuarios_inversiones_totales = []
            nombres_procesados_para_total = []
            for i in range(len(registro_transacciones)):
                usuario = registro_transacciones[i][0]
                total_invertido_transaccion = registro_transacciones[i][4]
                esta = False
                for j in range(len(nombres_procesados_para_total)):
                    if nombres_procesados_para_total[j] == usuario:
                        esta = True
                        for k in range(len(usuarios_inversiones_totales)):
                            if usuarios_inversiones_totales[k][0] == usuario:
                                usuarios_inversiones_totales[k][1] += total_invertido_transaccion
                                break
                        break
                if not esta:
                    usuarios_inversiones_totales += [[usuario, total_invertido_transaccion]]
                    nombres_procesados_para_total += [usuario]
            for i in range(len(usuarios_inversiones_totales)):
                if usuarios_inversiones_totales[i][1] > promedio_inversion:
                    usuarios_superan_res += [usuarios_inversiones_totales[i][0]]
            if not usuarios_superan_res:
                print("Ningún usuario supera la inversión promedio.")
            else:
                for i in range(len(usuarios_superan_res)):
                    print(f"👤 {usuarios_superan_res[i]}")
    return None

def ejecutar_submenu_consultas(nombres_t: list, acciones_t: list, cantidades_t: list) -> None:
    """
    Muestra un submenú de consultas sobre las transacciones registradas y ejecuta la opción elegida por el usuario.

    Args:
        nombres_t (list): Lista con los nombres de usuarios que realizaron transacciones.
        acciones_t (list): Lista con los nombres de las empresas cuyas acciones fueron adquiridas.
        cantidades_t (list): Lista con la cantidad de acciones compradas por cada usuario.

    Comportamiento:
    - Si no hay transacciones registradas (nombres_t = vacío), muestra un mensaje de advertencia.
    - Construye el "registro_transacciones" con los datos ingresados.
    - Presenta un submenú con diferentes opciones de consulta.
    - Valida la entrada del usuario para asegurarse de que es un número válido.
    - Ejecuta la función correspondiente a la opción seleccionada, gestionando los errores si la opción es inválida.
    - Permite al usuario volver al menú principal tras finalizar una consulta.

    Retorno:
    None
    """
    if not nombres_t:
        print("⚠️ Primero debe registrar transacciones (opción 1 del menú principal).")
    else:
        registro_transacciones = detallar_transacciones(nombres_t, acciones_t, cantidades_t)
        continuar_submenu = True
        while continuar_submenu:
            print("\n📋 Submenú de Consultas:")
            print("  1. Cantidad total de acciones por usuario.")
            print("  2. Promedio de acciones por empresa.")
            print("  3. Usuarios (Z-A) con total invertido.")
            print("  4. Inversión total acumulada.")
            print("  5. Empresa con más acciones por usuario.")
            print("  6. Acción con mayor inversión total (USD).")
            print("  7. Porcentaje de inversión por usuario.")
            print("  8. Usuarios que superan la inversión promedio.")
            print("  9. Volver al menú principal.")
            opcion_str = input("Seleccione una opción de consulta: ")
            es_opcion_valida_formato = True
            if not opcion_str: es_opcion_valida_formato = False
            else:
                for i in range(len(opcion_str)):
                    if not reconocer_numero(opcion_str[i]):
                        es_opcion_valida_formato = False
                        break
            if not es_opcion_valida_formato:
                print("Error: Opción inválida, ingrese un número.")
                continue
            opcion_consulta = int(opcion_str)

            match opcion_consulta:
                case 1:
                    consultar_total_acciones(registro_transacciones)
                case 2:
                    consultar_promedio_empresas(registro_transacciones)
                case 3:
                    consultar_usuarios_total(registro_transacciones)
                case 4:
                    total_g = consultar_inversion_total(registro_transacciones)
                    print(f"\n💲 Inversión Total Acumulada: ${total_g:.2f} USD")
                case 5:
                    consultar_acciones_usuario(registro_transacciones)
                case 6:
                    consultar_mayor_accion(registro_transacciones)
                case 7:
                    consulta_porcentaje_inversion_por_usuario(registro_transacciones)
                case 8:
                    consulta_usuarios_superan_promedio_inversion(registro_transacciones)
                case 9:
                    print("↩️ Volviendo al menú principal...")
                    continuar_submenu = False
                case _:
                    print("❌ Opción de consulta no válida.")

            if continuar_submenu:
                input("\nPresione Enter para continuar en Consultas...")

    return None

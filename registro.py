from normalizacion import normalizar_nombre_usuario, normalizar_empresas
from utilidades import reconocer_numero
from datos import vip_normalizados, empresas_normalizadas, precios

def registrar_usuario():
    """
    Solicita el ingreso de un nombre de usuario y valida que esté en la lista de usuarios VIP.

    Comportamiento:
    - Solicita un nombre de usuario al usuario.
    - Verifica que el campo ingresado no esté vacío.
    - Normaliza el nombre para que tenga la primera letra en mayúscula y el resto en minúsculas.
    - Busca el usuario en la lista de usuarios VIP.
    - Si el usuario está en la lista, lo valida y retorna; de lo contrario, muestra un mensaje de error y vuelve a solicitar el ingreso.

    Retorno:
    - (str): Nombre del usuario validado y normalizado.
    """
    usuario_validado = ""
    
    usuario_ok = False
    while not usuario_ok:
        usuario_ingresado = input("Ingrese nombre del usuario: ")
        if not usuario_ingresado:
            print("Error: El nombre de usuario no puede estar vacío.")
            continue
        usuario_normalizado = normalizar_nombre_usuario(usuario_ingresado)
        esta_en_la_lista = False
        for i in range(len(vip_normalizados)):
            if vip_normalizados[i] == usuario_normalizado:
                esta_en_la_lista = True
                break
        if esta_en_la_lista:
            usuario_validado = usuario_normalizado
            usuario_ok = True
        else:
            print(f"Error: Usuario '{usuario_ingresado}' no encontrado en la lista de usuarios VIP.")

    print(f"  Usuario: {usuario_validado}")    
    return usuario_validado

def registrar_empresa():
    """
    Solicita el ingreso del nombre de una acción y valida que sea una opción permitida.

    Comportamiento:
    - Pide al usuario que ingrese el nombre de una acción.
    - Verifica que el campo ingresado no esté vacío.
    - Normaliza el nombre de la acción (todo en mayúsculas).
    - Busca la acción en la lista de empresas permitidas.
    - Si la acción está en la lista, la valida y la retorna; de lo contrario, muestra un mensaje de error y vuelve a solicitar el ingreso.

    Retorno:
    - (str): Nombre de la acción validada y normalizada.
    """
    empresa_validada = ""

    empresa_ok = False
    while not empresa_ok:
        accion_ingresada = input(f"Ingrese nombre de la acción (Apple, Tesla, Nvidia): ")
        if not accion_ingresada:
            print("Error: El nombre de la acción no puede estar vacío.")
            continue
        accion_ingresada_normalizada = normalizar_empresas(accion_ingresada)
        esta_en_la_lista = False
        for i in range(len(empresas_normalizadas)):
            if empresas_normalizadas[i] == accion_ingresada_normalizada:
                esta_en_la_lista = True
                break
        if esta_en_la_lista:
            empresa_validada = accion_ingresada_normalizada
            empresa_ok = True
        else:
            print(f"Error: Acción '{accion_ingresada}' no válida. Elija entre Apple, Tesla o Nvidia.")
    print(f"  Acción: {empresa_validada}")
    return empresa_validada

def registrar_cantidad():
    """
    Solicita al usuario una cantidad de acciones a comprar y valida el ingreso.

    Comportamiento:
    - Pide al usuario que ingrese un número de acciones dentro del rango permitido (0 - 500).
    - Verifica que el campo no esté vacío.
    - Recorre cada carácter de la entrada para confirmar que solo contiene números.
    - Convierte la entrada en un entero y valida que esté dentro del rango permitido.
    - Si el número es válido, lo retorna; de lo contrario, muestra mensajes de error y solicita nuevamente el ingreso.

    Retorno:
    - (int): Cantidad de acciones validada.
    """    
    cantidad_ok = False
    min_cantidad = 0
    max_cantidad = 500
    while not cantidad_ok:
        cantidad_ingresada = input(f"Ingrese cantidad de acciones que desea comprar ({min_cantidad}-{max_cantidad}): ")
        formato_valido = True
        if not cantidad_ingresada:
            print("Error: La cantidad no puede estar vacía.")
            formato_valido = False
        else:
            for i in range(len(cantidad_ingresada)):
                if not reconocer_numero(cantidad_ingresada[i]):
                    formato_valido = False
                    break
        if formato_valido:
            cantidad_parseada = int(cantidad_ingresada)
            if min_cantidad <= cantidad_parseada <= max_cantidad:
                cantidad_validada = cantidad_parseada
                cantidad_ok = True
            else:
                print(f"Error: La cantidad debe estar entre {min_cantidad} y {max_cantidad}.")
        else:
            print("Error: Formato de cantidad no válido. Ingrese solo números enteros.")
    print(f"  Cantidad: {cantidad_validada}")

    return cantidad_validada

def obtener_precio(accion_normalizada_buscada: str) -> float:
    """
    Obtiene el precio en USD de una acción específica.

    Args:
        accion_normalizada_buscada (str): Nombre de la acción normalizado en mayúsculas.

    Comportamiento:
    - Recorre la lista `empresas_normalizadas` para encontrar la acción buscada.
    - Si la acción está en la lista, devuelve su precio correspondiente desde `precios`.
    - Si no se encuentra la acción, retorna 0.0.

    Retorno:
    - (float): Precio de la acción en USD.
    """
    precio_obtenido = 0.0
    for i in range(len(empresas_normalizadas)):
        if empresas_normalizadas[i] == accion_normalizada_buscada:
            precio_obtenido = precios[i]
            break
    return precio_obtenido

def detallar_transacciones(nombres_t: list, acciones_t: list, cantidades_t: list) -> list:
    """
    Genera un registro de transacciones con información detallada sobre cada compra de acciones.

    Args:
        nombres_t (list): Lista de nombres de usuarios que realizaron transacciones.
        acciones_t (list): Lista de nombres de empresas cuyas acciones fueron adquiridas.
        cantidades_t (list): Lista con las cantidades de acciones compradas por cada usuario.

    Comportamiento:
    - Recorre las listas de nombres, acciones y cantidades para construir un registro estructurado.
    - Obtiene el precio unitario de cada acción con "obtener_precio()".
    - Calcula el total invertido multiplicando el precio unitario por la cantidad comprada.
    - Almacena cada transacción en una lista con la siguiente estructura:
        [usuario, empresa, precio por unidad, cantidad adquirida, total invertido].

    Retorno:
    - (list): Lista de transacciones con los detalles de cada compra.
    """
    registro_transacciones = []
    for i in range(len(nombres_t)):
        usuario = nombres_t[i]
        accion = acciones_t[i]
        cantidad = cantidades_t[i]
        precio_unitario = obtener_precio(accion)
        total_invertido = precio_unitario * (cantidad)
        registro_transacciones += [[usuario, accion, precio_unitario, cantidad, total_invertido]]
    return registro_transacciones

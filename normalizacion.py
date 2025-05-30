def normalizar_nombre_usuario(usuario: str) -> str:
    """
    Convierte el nombre de usuario en un formato estandarizado:
    - La primera letra en mayúscula.
    - El resto de los caracteres en minúscula.

    Args:
        usuario (str): Nombre de usuario a normalizar.

    Comportamiento:
    - Si el usuario está vacío, retorna una cadena vacía.
    - Convierte la primera letra a mayúscula si es una letra minúscula ('a' - 'z').
    - Recorre el resto de los caracteres y convierte cualquier mayúscula ('A' - 'Z') en minúscula.
    - Retorna el nombre formateado.

    Retorno:
    - (str): Nombre de usuario con la primera letra en mayúscula y el resto en minúscula.
    """
    nombre_normalizado = ""
    if usuario:
        primera_letra = ord(usuario[0])
        if ord('a') <= primera_letra <= ord('z'):
            nombre_normalizado += chr(primera_letra - 32)
        else:
            nombre_normalizado += usuario[0]
        for i in range(1, len(usuario)):
            orden_caracter = ord(usuario[i])
            if ord('A') <= orden_caracter <= ord('Z'):
                nombre_normalizado += chr(orden_caracter + 32)
            else:
                nombre_normalizado += usuario[i]
    return nombre_normalizado

def normalizar_empresas(empresa: str) -> str:
    """
    Convierte el nombre de una empresa a mayúsculas sin usar métodos de cadena.

    Args:
        empresa (str): Nombre de la empresa a normalizar.

    Comportamiento:
    - Recorre cada carácter de la cadena `empresa`.
    - Convierte caracteres en minúscula ('a' - 'z') a mayúscula restando 32 en su código ASCII.
    - Si el carácter ya está en mayúscula, lo mantiene sin cambios.
    - Construye y retorna el nombre normalizado.

    Retorno:
    - (str): Nombre de la empresa con todas las letras en mayúsculas.
    """
    nombre_normalizado = ""
    if empresa:
        for i in range(len(empresa)):
            caracter_ascii = ord(empresa[i])
            if ord('a') <= caracter_ascii <= ord('z'):
                nombre_normalizado += chr(caracter_ascii - 32)
            else:
                nombre_normalizado += empresa[i]
    return nombre_normalizado

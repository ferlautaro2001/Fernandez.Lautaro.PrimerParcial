def reconocer_numero(caracter: str) -> bool:
    """
    Verifica si un carácter dado es un número entre '0' y '9'.

    Args:
        caracter (str): Carácter a evaluar.

    Comportamiento:
    - Comprueba si el carácter está dentro del rango de '0' a '9'.
    - Si el carácter es un número, devuelve True.
    - Si no lo es, devuelve False.

    Retorno:
    - (bool): True si es un número, False en caso contrario.
    """
    es_numero = False
    if '0' <= caracter <= '9':
        es_numero = True
    return es_numero

def ordenar_alfabeticamente(lista: list, indice: int, descendente: bool = False) -> None:
    """
    Ordena una lista de listas alfabéticamente según el índice especificado.

    Args:
        lista (list): Lista de listas donde cada sublista contiene al menos un elemento en la posición `indice`.
        indice (int): Posición dentro de cada sublista por la cual se realizará la ordenación.
        descendente (bool, opcional): Define si la ordenación será de mayor a menor (Z-A). Por defecto es False (A-Z).

    Comportamiento:
    - Recorre la lista de listas y aplica el algoritmo de ordenamiento burbuja para organizar los elementos.
    - Si `descendente` es True, ordena de Z-A; si es False, ordena de A-Z.
    - No retorna ningún valor, ya que modifica "lista" directamente.

    Retorno:
    None
    """
    for i in range(len(lista) - 1):
        for j in range(0, len(lista) - i - 1):
            condicion_swap = False
            if descendente:
                if lista[j][indice] < lista[j+1][indice]:
                    condicion_swap = True
            else:
                if lista[j][indice] > lista[j+1][indice]:
                    condicion_swap = True
            if condicion_swap:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return None

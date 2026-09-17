"""Reglas de promoción y cálculo de importes."""

# Valores de descuento por tipo
REGLAS_DESCUENTO = {
    "ninguno": 0.0,
    "porcentaje": 0.10,
    "mayorista": 0.15,
    "3x2": "paga dos y selecciona tres",
}

def calcular_subtotal(carrito, catalogo):
    """Suma precio por cantidad de todos los artículos del carrito.

    Args:
        carrito (list[tuple[str, int]]): Productos seleccionados.
        catalogo (dict): Productos disponibles.

    Returns:
        float: Subtotal sin descuentos.
    """
    subtotal = 0.0
    for identificador, cantidad in carrito:
        subtotal += catalogo[identificador]["precio"] * cantidad  # precio x cantidad
    return subtotal


def calcular_descuento_3x2(carrito, catalogo):
    """Calcula el importe gratuito para productos elegibles en promoción 3x2.

    Los productos cuyo ID termina en un número impar participan en esta
    promoción de ejemplo. El condicional anidado dentro del ciclo identifica
    cada artículo elegible y cuenta sus grupos de tres.

    Args:
        carrito (list[tuple[str, int]]): Artículos seleccionados.
        catalogo (dict): Datos de los productos.

    Returns:
        float: Importe que se debe restar al subtotal.
    """
    descuento = 0.0
    for identificador, cantidad in carrito:
        if int(identificador[-1]) % 2 != 0:  # ID impar = elegible
            grupos_de_tres = cantidad // 3  # paquetes completos de 3
            if grupos_de_tres > 0:
                descuento += grupos_de_tres * catalogo[identificador]["precio"]  # 1 gratis por paquete
    return round(descuento, 2)

def aplicar_descuento(subtotal, tipo_descuento, carrito=None, catalogo=None):
    """Aplica una regla de descuento al subtotal.

    Args:
        subtotal (float): Importe antes de descuentos.
        tipo_descuento (str): Regla elegida: ninguno, porcentaje, mayorista o 3x2.
        carrito (list[tuple[str, int]], optional): Requerido solo si tipo_descuento es "3x2".
        catalogo (dict, optional): Requerido solo si tipo_descuento es "3x2".

    Returns:
        float: Total ajustado y redondeado a dos decimales.
    """
    tipo_descuento = tipo_descuento.lower()  # ignora mayúsculas/minúsculas
    if tipo_descuento == "ninguno":
        return round(subtotal, 2)
    elif tipo_descuento == "porcentaje":
        return round(subtotal * (1 - REGLAS_DESCUENTO["porcentaje"]), 2)
    elif tipo_descuento == "mayorista":
        if subtotal >= 200:  # mínimo requerido
            return round(subtotal * (1 - REGLAS_DESCUENTO["mayorista"]), 2)
        print("El descuento mayorista requiere una compra mínima de $200.00.")
        return round(subtotal, 2)
    elif tipo_descuento == "3x2":
        if carrito is None or catalogo is None:  # datos obligatorios
            print("La promoción 3x2 requiere el carrito y el catálogo.")
            return round(subtotal, 2)
        descuento = calcular_descuento_3x2(carrito, catalogo)
        return round(subtotal - descuento, 2)
    else:
        print("Tipo de descuento no válido; no se aplicó descuento.")
        return round(subtotal, 2)

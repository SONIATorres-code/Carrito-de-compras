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



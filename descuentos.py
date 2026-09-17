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


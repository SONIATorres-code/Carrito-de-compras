"""Generación del resumen de venta inmutable."""

from datetime import date

def generar_ticket(carrito, catalogo, total):
    """Imprime el resumen de compra y devuelve el registro de venta.

    Args:
        carrito (list[tuple[str, int]]): Artículos comprados.
        catalogo (dict): Datos de los productos.
        total (float): Importe final a pagar.

    Returns:
        tuple[str, str, float]: Folio, fecha ISO y total de la venta.
    """


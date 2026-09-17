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
    folio = f"F{date.today():%Y%m%d}"
    fecha = date.today().isoformat()
    print("\n======= TICKET DE COMPRA =======")
    print(f"Folio: {folio}\nFecha: {fecha}")
    for identificador, cantidad in carrito:
        producto = catalogo[identificador]
        print(f"{producto['nombre']}: {cantidad} x ${producto['precio']:.2f}")
    print(f"TOTAL PAGADO: ${total:.2f}")
    print("================================")
    return (folio, fecha, total)

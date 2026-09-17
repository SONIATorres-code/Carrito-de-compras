def cargar_catalogo():
    """Retorna el catalogo de productos en un diccionario de diccionarios."""
    catalogo = {
        "P001": {"nombre": "Cafe Americano", "precio": 45.0, "stock": 20},
        "P002": {"nombre": "Capuchino",      "precio": 55.0, "stock": 18},
        "P003": {"nombre": "Pay de Limon",   "precio": 35.0, "stock": 10},
        "P004": {"nombre": "Te Verde",       "precio": 40.0, "stock": 12},
        "P005": {"nombre": "Sandwich Jamon", "precio": 38.0, "stock": 8}
        "P006": {"nombre": "Muffin Vainilla", "precio": 28.0, "stock": 10},
    }
    return catalogo


def mostrar_catalogo(catalogo):
    """Muestra los productos disponibles en formato de tabla en consola."""
    if not catalogo:
        print("\n[!] El catalogo se encuentra vacio.")
        return

    print("\n" + "=" * 55)
    print(f"{'CODIGO':<8} | {'PRODUCTO':<20} | {'PRECIO':<10} | {'STOCK':<6}")
    print("=" * 55)
    for id_prod, info in catalogo.items():
        nombre = info["nombre"]
        precio = f"${info['precio']:.2f}"
        stock = info["stock"]
        print(f"{id_prod:<8} | {nombre:<20} | {precio:<10} | {stock:<6}")
    print("=" * 55 + "\n")
def cargar_catalogo():
    catalogo = {
        "P001": {"nombre": "Cafe Americano", "precio": 45.0, "stock": 20},
        "P001": {"nombre": "Capuchino", "precio": 55.0, "stock": 18},
        "P001": {"nombre": "Pay de Limón", "precio": 35.0, "stock": 10},
        "P001": {"nombre": "Té Verde", "precio": 40.0, "stock": 12},
        "P001": {"nombre": "Sandwich Jamón", "precio": 38.0, "stock": 8}
    }
    return catalogo 

def mostrar_catalogo(catalogo): 
    print("\n" + "=" * 55)
    print(f"{'CÓDIGO':<8} | {'PRODUCTO':<20 | {'PRECIO': <10} | {'STOCK': <6}")
    print("=" * 55)
    for id_prod, info in catalogo.items():
        nombre = info["nombre"]
        precio = f"${info['precio']:.2f}"
        stock = info["stock"]
        print(f"{id_prod:<8} | {nombre:<20} | {precio:<10} | {stock:<6}")
    print("=" * 55 + "\n")
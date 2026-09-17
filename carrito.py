"""Operaciones para administrar una lista de tuplas de compra."""


def agregar_producto(carrito, catalogo, id_producto, cantidad):
    """Agrega o incrementa un producto cuando existe stock suficiente.

    Args:
        carrito (list[tuple[str, int]]): Productos y cantidades seleccionadas.
        catalogo (dict): Catálogo que contiene precios y existencias.
        id_producto (str): Identificador del producto solicitado.
        cantidad (int): Unidades que se desean agregar.

    Returns:
        list[tuple[str, int]]: Carrito actualizado; no cambia si falla la validación.
    """
    id_producto = id_producto.upper()
    if id_producto not in catalogo:
        print("El ID de producto no existe.")
    elif cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
    else:
        cantidad_actual = next(
            (cantidad_carrito for codigo, cantidad_carrito in carrito
             if codigo == id_producto),
            0,
        )
        if cantidad_actual + cantidad > catalogo[id_producto]["stock"]:
            print("Stock insuficiente para la cantidad solicitada.")
        else:
            for indice, (codigo, cantidad_carrito) in enumerate(carrito):
                if codigo == id_producto:
                    carrito[indice] = (codigo, cantidad_carrito + cantidad)
                    break
            else:
                carrito.append((id_producto, cantidad))
            print("Producto agregado al carrito.")
    return carrito


def eliminar_producto(carrito, id_producto):
    """Elimina del carrito el producto indicado.

    Args:
        carrito (list[tuple[str, int]]): Carrito actual.
        id_producto (str): ID a eliminar.

    Returns:
        list[tuple[str, int]]: Carrito sin el producto indicado.
    """
    id_producto = id_producto.upper()
    if not carrito:
        print("El carrito está vacío.")
    else:
        for item in carrito:
            if item[0] == id_producto:
                carrito.remove(item)
                print("Producto eliminado del carrito.")
                break
        else:
            print("Ese producto no está en el carrito.")
    return carrito


def mostrar_carrito(carrito, catalogo):
    """Muestra el contenido actual y el importe por línea del carrito."""
    if not carrito:
        print("\nEl carrito está vacío.")
        return
    print("\n--- CARRITO ---")
    for identificador, cantidad in carrito:
        producto = catalogo[identificador]
        importe = producto["precio"] * cantidad
        print(f"{identificador} - {producto['nombre']}: {cantidad} x "
              f"${producto['precio']:.2f} = ${importe:.2f}")

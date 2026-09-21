"""Punto de entrada del programa: menú principal del carrito de compras."""

from catalogo import cargar_catalogo, mostrar_catalogo
from carrito import agregar_producto, eliminar_producto, mostrar_carrito
from descuentos import calcular_subtotal, aplicar_descuento
from ticket import generar_ticket


def main():
    """Ejecuta el menú principal del programa en un ciclo hasta que el usuario salga."""
    catalogo = cargar_catalogo()
    carrito = []

    while True:
        print("\n=== CARRITO DE COMPRAS ===")
        print("1. Ver catálogo")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Ver carrito")
        print("5. Checkout / generar ticket")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_catalogo(catalogo)
        elif opcion == "2":
            id_producto = input("ID del producto: ")
            cantidad = int(input("Cantidad: "))
            carrito = agregar_producto(carrito, catalogo, id_producto, cantidad)
        elif opcion == "3":
            id_producto = input("ID del producto a eliminar: ")
            carrito = eliminar_producto(carrito, id_producto)
        elif opcion == "4":
            mostrar_carrito(carrito, catalogo)
        elif opcion == "5":
            if not carrito:
                print("El carrito está vacío.")
                continue
            subtotal = calcular_subtotal(carrito, catalogo)
            tipo_descuento = input("Tipo de descuento (ninguno/porcentaje/mayorista/3x2): ")
            total = aplicar_descuento(subtotal, tipo_descuento, carrito, catalogo)
            generar_ticket(carrito, catalogo, total)
            carrito = []
        elif opcion == "6":
            print("¡Gracias por su compra!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()


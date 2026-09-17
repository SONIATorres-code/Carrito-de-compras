# Carrito-de-compras



\# Bitácora de Desarrollo - Módulo de Carrito de Compras



\## 1. Funciones Desarrolladas (`carrito.py`)



\* \*\*`agregar\_producto(carrito, producto, cantidad)`\*\*: Permite añadir un producto al carrito de compras o actualizar su cantidad si ya existe. Incluye validaciones para comprobar que el producto esté disponible en el catálogo y que la cantidad solicitada no supere el stock disponible.

\* \*\*`eliminar\_producto(carrito, producto)`\*\*: Permite remover un producto específico del carrito. Valida primero que el producto se encuentre en la lista antes de proceder con su eliminación.



\---



\## 2. Justificación de Estructuras de Datos



\* \*\*Catálogo (Diccionario)\*\*: Se utilizó una estructura de \*\*diccionario\*\* (`dict`) porque ofrece una búsqueda en tiempo constante $O(1)$ mediante claves únicas (nombres de los productos), facilitando la consulta inmediata de precios y stock.

\* \*\*Carrito de Compras (Lista de Tuplas)\*\*: Se implementó una \*\*lista de tuplas\*\* (`list\[tuple]`) para representar los elementos del carrito, garantizando el orden de inserción de los productos y la inmutabilidad de los pares `(producto, cantidad)` registrados.


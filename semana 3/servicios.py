def agregar_producto(inventario, nombre, precio, cantidad):

    #Agrega un producto al inventario.
    for producto in inventario:
        if producto["nombre"] == nombre:
            return False
        
    inventario.append({
        "nombre": nombre, 
        "precio": float(precio), 
        "cantidad": int(cantidad)
    })
    return True

def mostrar_inventario(inventario: list):

    #Muestra todos los productos en el inventario.
    if not inventario:
        print("Inventario vacío.")
        return
    print("\n=== INVENTARIO ===")
    for p in inventario:
        print(f"Nombre: {p['nombre']}, Precio: ${p['precio']:}, Cantidad: {p['cantidad']}")
    print(f"  Total de productos: {len(inventario)}\n")

def buscar_producto(inventario, nombre):

    #Busca un producto por nombre.
    for prod in inventario:
        if prod["nombre"] == nombre:
            return prod
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):

    #Actualiza precio o cantidad de un producto.
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print(f"Producto '{nombre}' no encontrado.")
        return False
    if nuevo_precio is not None:
        producto["precio"] = float(nuevo_precio)
    if nueva_cantidad is not None:
        producto["cantidad"] = int(nueva_cantidad)
    
    print(f"Producto '{nombre}' actualizado: "
        f"precio=${producto['precio']:}, cantidad={producto['cantidad']}")
    return True

def eliminar_producto(inventario, nombre):

    #Elimina un producto por nombre.
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print(f"Producto '{nombre}' no encontrado.")
        return False
    inventario.remove(producto)
    print(f"Producto '{nombre}' eliminado del inventario.")
    return True

def calcular_estadisticas(inventario):
    
    #Calcula estadísticas del inventario.
    if not inventario:
        return None
    
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    
    return {
    "unidades_totales": unidades_totales,
            "valor_total": valor_total,
            "producto_mas_caro": {"nombre": producto_mas_caro["nombre"], "precio": producto_mas_caro["precio"]},
            "producto_mayor_stock": {"nombre": producto_mayor_stock["nombre"], "cantidad": producto_mayor_stock["cantidad"]}
        }


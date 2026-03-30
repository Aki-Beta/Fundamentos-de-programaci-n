#Se llama a los servicios y archivos para usar sus funciones en el menú de la aplicación.

from servicios import *
from archivos import *

def main():
    #Menú principal del programa.
    inventario = []
    continuar = True  # Variable de control del while

    while continuar:
        print("\n" + "="*40)
        print("      MENÚ DE INVENTARIO")
        print("="*40)
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Ver estadísticas")
        print("7. Guardar inventario")
        print("8. Cargar inventario")
        print("9. Salir")
        print("="*40)
        
        try:
        #Se valida que la opción ingresada sea un número entero.
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Opción inválida. Debe ser un número.")
            continue
        
        if opcion == 1:
            nombre = input("Nombre: ").strip()
            try:
                
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                if precio < 0 or cantidad < 0:
                    print("Precio y cantidad deben ser no negativos.")
                    continue
                if agregar_producto(inventario, nombre, precio, cantidad):
                    print(f"Producto '{nombre}' agregado.")
                else:
                    print(f"Producto '{nombre}' ya existe.")
            except ValueError:
                print("Precio y cantidad deben ser numéricos.")
                return 
        
        elif opcion == 2:
            mostrar_inventario(inventario)
        
        elif opcion == 3:
            nombre = input("Nombre a buscar: ").strip()
            prod = buscar_producto(inventario, nombre)
            if prod:
                print(f"Encontrado: {prod}")
            else:
                print(f"Producto '{nombre}' no encontrado.")
        
        elif opcion == 4:
            nombre = input("Nombre a actualizar: ").strip()
            prod = buscar_producto(inventario, nombre)
            if not prod:
                print(f"Producto '{nombre}' no encontrado.")
                continue
            nuevo_precio = input("Nuevo precio (dejar vacío para no cambiar): ").strip()
            nueva_cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ").strip()
            precio = float(nuevo_precio) if nuevo_precio else None
            cantidad = int(nueva_cantidad) if nueva_cantidad else None
            if actualizar_producto(inventario, nombre, precio, cantidad):
                print(f"Producto '{nombre}' actualizado.")
            else:
                print(f"Error al actualizar '{nombre}'.")
        
        elif opcion == 5:
            nombre = input("Nombre a eliminar: ").strip()
            if eliminar_producto(inventario, nombre):
                print(f"Producto '{nombre}' eliminado.")
            else:
                print(f"Producto '{nombre}' no encontrado.")
        
        elif opcion == 6:
            stats = calcular_estadisticas(inventario)
            if not stats["producto_mas_caro"]:
                print(" Inventario vacío.")
            else:
                print(f"Estadísticas:")
                print(f"Unidades totales: {stats['unidades_totales']}")
                print(f"Valor total: ${stats['valor_total']:.2f}")
                print(f"Producto más caro: {stats['producto_mas_caro'] ['nombre']} (${stats['producto_mas_caro'] ['precio']:.2f})")
                print(f"Producto con mayor stock: {stats['producto_mayor_stock'] ['nombre']} ({stats['producto_mayor_stock'] ['cantidad']})")
        
        elif opcion == 7:
            ruta = input("Ruta para guardar (ej: inventario.csv): ").strip()
            guardar_csv(inventario, ruta)
        
        elif opcion == 8:
            ruta = input("Ruta del archivo a cargar: ").strip()
            nuevo_inventario, errores = cargar_csv(ruta)
            if not nuevo_inventario:
                continue
            accion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
            if accion == 'S':
                inventario = nuevo_inventario
                print("Inventario reemplazado.")
            else:
                # Fusión: actualizar cantidad si existe, agregar si no
                for prod in nuevo_inventario:
                    encontrado = False
                    for p in inventario:
                        if p["nombre"] == prod["nombre"]:
                            p["cantidad"] += prod["cantidad"]
                            if p["precio"] != prod["precio"]:
                                p["precio"] = prod["precio"]  # Actualizar precio si difiere
                            encontrado = True
                            break
                    if not encontrado:
                        inventario.append(prod)
                print(" Inventario fusionado.")
        
        elif opcion == 9:
            print("Gracias por comprar en nuestra tienda. ¡Hasta luego!")
            continuar = False  # Salimos del bucle
        
        else:
            print("Opción no válida. Elige entre 1 y 9.")

if __name__ == "__main__":
    main()
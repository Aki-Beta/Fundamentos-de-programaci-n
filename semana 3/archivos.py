import os
import csv
def guardar_csv(inventario, ruta, incluir_header=True):
    
    #Guarda el inventario en un archivo CSV.
    if not inventario:
        print("  Inventario vacío. No se guardó nada.")
        return 
    
    try:
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
            for producto in inventario:
                writer.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])
        print(f" Inventario guardado en: {ruta}")
        return True
    except Exception as e:
        print(f" Error al guardar: {e}")
    return False

def cargar_csv(ruta: str):
    """Carga inventario desde CSV.
    """
    productos = []     # filas válidas acumuladas
    errores = 0        # contador de filas inválidas

    try:
        with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            # Validar encabezado 
            try:
                encabezado = next(lector)
            except StopIteration:
                print("El archivo CSV está vacío.")
                return None

            encabezado_limpio = [col.strip().lower() for col in encabezado]
            if encabezado_limpio != ["nombre", "precio", "cantidad"]:
                print(f"Encabezado inválido: {encabezado}. "
                    f"Se esperaba: nombre,precio,cantidad")
                return None

            #  Procesar filas 
            for num_fila, fila in enumerate(lector, start=2):  # start=2: fila 1 = header

                # Validar número de columnas
                if len(fila) != 3:
                    print(f"Fila {num_fila} ignorada: se esperaban 3 columnas, "
                        f"se encontraron {len(fila)}.")
                    errores += 1
                    continue

                nombre, precio_str, cantidad_str = [col.strip() for col in fila]

                # Validar nombre no vacío
                if not nombre:
                    print(f"Fila {num_fila} ignorada: nombre vacío.")
                    errores += 1
                    continue

                # Convertir y validar precio
                try:
                    precio = float(precio_str)
                    if precio < 0:
                        raise ValueError("precio negativo")
                except ValueError:
                    print(f"Fila {num_fila} ignorada: precio inválido ('{precio_str}').")
                    errores += 1
                    continue

                # Convertir y validar cantidad
                try:
                    cantidad = int(cantidad_str)
                    if cantidad < 0:
                        raise ValueError("cantidad negativa")
                except ValueError:
                    print(f"Fila {num_fila} ignorada: cantidad inválida ('{cantidad_str}').")
                    errores += 1
                    continue
                # Fila válida → agregar al resultado
                productos.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })

    except FileNotFoundError:
        print(f"Archivo no encontrado: '{ruta}'.")
        return None

    except UnicodeDecodeError:
        print(f"Error de codificación al leer '{ruta}'. "
            f"Asegúrate de que el archivo esté en UTF-8.")
        return None

    except ValueError as e:
        print(f"Error de valor inesperado: {e}")
        return None

    except Exception as e:
        print(f"Error inesperado al leer '{ruta}': {e}")
        return None

    # Informe final de carga
    if errores > 0:
        print(f"{errores} fila(s) inválida(s) fueron omitidas.")

    print(f"  [OK] {len(productos)} producto(s) cargados desde '{ruta}'.")
    return productos

def fusionar_inventarios(inventario_actual: list, nuevos: list) -> int:
    """
    Fusiona una lista de productos nuevos al inventario actual.
    Retorna:
        Número de productos agregados (no actualizados).
    """
    agregados = 0

    for nuevo in nuevos:
        # Buscar si el nombre ya existe 
        existente = next(
            (p for p in inventario_actual
            if p["nombre"].lower() == nuevo["nombre"].lower()),
            None
        )

        if existente:
            # Actualizar precio y sumar cantidad
            existente["precio"] = nuevo["precio"]
            existente["cantidad"] += nuevo["cantidad"]
        else:
            inventario_actual.append(nuevo)
            agregados += 1

    return agregados
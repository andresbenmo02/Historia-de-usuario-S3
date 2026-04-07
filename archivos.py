import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("Inventario vacio. No se guarda.")
        return
    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if incluir_header:
                writer.writerow(["nombre","precio","cantidad"])
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])
        print(f"Inventario guardado en: {ruta}")
    except Exception as e:
        print(f"Error al guardar CSV: {e}")

def cargar_csv(ruta):
    inventario_cargado = []
    errores = 0
    try:
        with open(ruta, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != ["nombre","precio","cantidad"]:
                print("Archivo invalido. Encabezado incorrecto.")
                return [], 0
            for row in reader:
                try:
                    nombre = row["nombre"]
                    precio = float(row["precio"])
                    cantidad = int(row["cantidad"])
                    if precio<0 or cantidad<0:
                        errores += 1
                        continue
                    inventario_cargado.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except:
                    errores += 1
        return inventario_cargado, errores
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return [], 0
    except Exception as e:
        print(f"Error al leer CSV: {e}")
        return [], 0
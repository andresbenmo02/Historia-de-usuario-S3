from servicios import *
from archivos import *

inventario = []
continuar = True

while continuar:
    print("\n--- MENU INVENTARIO ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadisticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Seleccione opcion (1-9): ")

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        agregar_producto(inventario, nombre, precio, cantidad)
        print("Producto agregado.")
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        p = buscar_producto(inventario, nombre)
        if p:
            print(f"Encontrado: {p}")
        else:
            print("Producto no encontrado.")
    elif opcion == "4":
        nombre = input("Nombre a actualizar: ")
        nuevo_precio = input("Nuevo precio (dejar vacio si no cambia): ")
        nueva_cantidad = input("Nueva cantidad (dejar vacio si no cambia): ")
        np = float(nuevo_precio) if nuevo_precio else None
        nc = int(nueva_cantidad) if nueva_cantidad else None
        if actualizar_producto(inventario, nombre, np, nc):
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")
    elif opcion == "5":
        nombre = input("Nombre a eliminar: ")
        if eliminar_producto(inventario, nombre):
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")
    elif opcion == "6":
        stats = calcular_estadisticas(inventario)
        if stats:
            print(f"Unidades totales: {stats['unidades_totales']}")
            print(f"Valor total: {stats['valor_total']}")
            print(f"Producto mas caro: {stats['producto_mas_caro']}")
            print(f"Producto mayor stock: {stats['producto_mayor_stock']}")
        else:
            print("Inventario vacio.")
    elif opcion == "7":
        ruta = input("Ruta para guardar CSV: ")
        guardar_csv(inventario, ruta)
    elif opcion == "8":
        ruta = input("Ruta para cargar CSV: ")
        cargado, errores = cargar_csv(ruta)
        if cargado:
            decision = input("Sobrescribir inventario actual? (S/N): ").lower()
            if decision == "s":
                inventario = cargado
                print(f"Inventario reemplazado. {len(cargado)} productos cargados, {errores} errores.")
            else:
                for p in cargado:
                    existente = buscar_producto(inventario, p["nombre"])
                    if existente:
                        existente["cantidad"] += p["cantidad"]
                        existente["precio"] = p["precio"]
                    else:
                        inventario.append(p)
                print(f"Inventario fusionado. {len(cargado)} productos cargados, {errores} errores.")
    elif opcion == "9":
        print("Saliendo del programa...")
        continuar = False
    else:
        print("Opcion invalida.")
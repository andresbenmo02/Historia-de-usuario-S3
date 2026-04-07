def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)

def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacio.")
    else:
        for p in inventario:
            print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")

def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    p = buscar_producto(inventario, nombre)
    if p:
        if nuevo_precio is not None:
            p["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            p["cantidad"] = nueva_cantidad
        return True
    return False

def eliminar_producto(inventario, nombre):
    p = buscar_producto(inventario, nombre)
    if p:
        inventario.remove(p)
        return True
    return False

def calcular_estadisticas(inventario):
    if not inventario:
        return None
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"]*p["cantidad"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
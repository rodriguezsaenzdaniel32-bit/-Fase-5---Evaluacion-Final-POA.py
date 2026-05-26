# Fase 5 - Evaluacion Final POA
#Daniel Rodriguez

# Problema 2: Gestion de precios de un menu de restaurante

# Matriz del menu
# [Nombre del Producto, Categoria, Precio Base]

menu = [
    ["Hamburguesa", "Comida Rapida", 25000],
    ["Pizza", "Comida Rapida", 32000],
    ["Ensalada Casar", "Saludable", 18000],
    ["Salmon", "Mariscos", 45000],
    ["Pasta Alfredo", "Italiana", 28000],
    ["Helado", "Postre", 12000]]

# Funcion para calcular el precio final
def calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral):
    """
    Aplica un 15% de descuento si:
    - La categoria coincide con la categoria objetivo
    - El precio base es mayor al umbral
    """

    # Validar que el precio sea numerico
    precio_base = float(precio_base)

    # Aplicar descuento
    if categoria == categoria_objetivo and precio_base > umbral:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base

    return precio_final


# Variables de la promocion
categoria_objetivo = "Comida Rapida"
umbral_precio = 20000

# Mostrar resultados
print("=== MENU DEL RESTAURANTE ===\n")

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # Calcular precio final
    precio_final = calcular_precio_final(
        categoria,
        precio_base,
        categoria_objetivo,
        umbral_precio)

    # Mostrar informacion
    print(f"Producto: {nombre}")
    print(f"Categoria: {categoria}")
    print(f"Precio Base: ${precio_base:,.0f}")
    print(f"Precio Final: ${precio_final:,.0f}")
    print("-" * 40)
# Documento 3 - TP6
# Alumno/a: Axel Ramirez

# -----------------------------
# Ejercicio 1: Ubipark
# -----------------------------
espacios = [True, False, True, True, False]  # True = libre, False = ocupado

libres = espacios.count(True)
print("Ejercicio 1 - Ubipark")
print("Espacios libres:", libres)
print()

# -----------------------------
# Ejercicio 2: Planeta Modo Off
# -----------------------------
consumo = 320  # en kWh

print("Ejercicio 2 - Planeta Modo Off")
if consumo > 300:
    print("Consumo alto. ¡Reducí el uso de energía!")
else:
    print("Buen trabajo ahorrando energía.")
print()

# -----------------------------
# Ejercicio 3: Civic Report
# -----------------------------
def reportar_bache(ubicacion):
    print("Bache reportado en:", ubicacion)

print("Ejercicio 3 - Civic Report")
reportar_bache("Calle 123, esquina San Martín")
print()

# -----------------------------
# Ejercicio 4: SafeZone
# -----------------------------
zona = "Parque Central"
puntuacion_seguridad = 8  # de 0 a 10

print("Ejercicio 4 - SafeZone")
if puntuacion_seguridad >= 7:
    print(zona, "es una zona segura.")
else:
    print(zona, "tiene riesgo. Tomá precauciones.")
print()

# -----------------------------
# Ejercicio 5: Collila Amigables
# -----------------------------
lugar = "cesto"  # opciones: "cesto", "suelo"

print("Ejercicio 5 - Collila Amigables")
if lugar == "cesto":
    print("¡Gracias por cuidar el ambiente!")
else:
    print("Por favor, usá los cestos de colillas.")

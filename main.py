import os

# VULNERABILIDAD / SECURITY HOTSPOT: Credencial expuesta en código
DB_PASSWORD = "SuperSecretPassword123!"

def calcular_promedio(valores):
    # CODE SMELL: Comparación explícita e ineficiencia en cálculo
    if len(valores) == 0:
        return 0
    suma = 0
    for v in valores:
        suma += v
    return suma / len(valores)

# CODE SMELL: Función no utilizada (Dead Code)
def funcion_inutil():
    pass
import os

# SOLUCIÓN: Cargar la variable de entorno directamente sin valores hardcodeados
DB_PASSWORD = os.getenv("DB_PASSWORD")

def calcular_promedio(valores):
    if not valores:
        return 0
    return sum(valores) / len(valores)
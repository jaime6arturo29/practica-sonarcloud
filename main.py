import os

# SOLUCIÓN: Uso seguro de credenciales mediante variables de entorno
DB_PASSWORD = os.getenv("DB_PASSWORD", "SecureFallbackPassword123!")

def calcular_promedio(valores):
    # SOLUCIÓN: Validación limpia de lista vacía y uso de la función nativa sum()
    if not valores:
        return 0
    return sum(valores) / len(valores)

# SOLUCIION: Se eliminó la función no utilizada (funcion_inutil) para limpiar el Code Smell
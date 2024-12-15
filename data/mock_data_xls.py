import pandas as pd
import random

# Generar datos simulados
data = {
    "Temperatura (°C)": [round(random.uniform(10, 50), 1) for _ in range(20)],
    "Recuento de Bacterias (UFC/ml)": [random.randint(100, 10000) for _ in range(20)],
}

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar como archivo Excel
df.to_excel("temperatura_bacterias.xlsx", index=False)

print("Archivo Excel generado: temperatura_bacterias.xlsx")

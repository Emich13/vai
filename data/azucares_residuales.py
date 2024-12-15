import pandas as pd
import random

# Generar datos simulados
data = {
    "Batch": [f"Batch-{i}" for i in range(1, 21)],
    "Día": [random.randint(1, 30) for _ in range(20)],
    "Azúcares Residuales (%)": [round(random.uniform(0, 10), 2) for _ in range(20)],
}

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar como archivo Excel
df.to_excel("azucares_residuales.xlsx", index=False)

print("Archivo Excel generado: azucares_residuales.xlsx")

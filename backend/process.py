import pandas as pd

def validate_excel(file_path, expected_columns):
    """
    Valida que el archivo Excel tenga las columnas necesarias.
    """
    try:
        data = pd.read_excel(file_path)
        missing_cols = [col for col in expected_columns if col not in data.columns]
        if missing_cols:
            return False, f"Faltan las columnas: {', '.join(missing_cols)}"
        return True, data
    except Exception as e:
        return False, str(e)

def process_temperature_bacteria(data):
    """
    Procesa los datos de temperatura vs recuento de bacterias para generar estadísticas descriptivas.
    """
    summary = {
        "Temperatura (\u00b0C)": {
            "Promedio": data["Temperatura (\u00b0C)"].mean(),
            "Mínimo": data["Temperatura (\u00b0C)"].min(),
            "Máximo": data["Temperatura (\u00b0C)"].max(),
        },
        "Recuento de Bacterias (UFC/ml)": {
            "Promedio": data["Recuento de Bacterias (UFC/ml)"].mean(),
            "Mínimo": data["Recuento de Bacterias (UFC/ml)"].min(),
            "Máximo": data["Recuento de Bacterias (UFC/ml)"].max(),
        },
    }
    return summary

def process_azucares(data):
    """
    Procesa los datos de azúcares residuales para generar estadísticas por batch.
    """
    summary = data.groupby("Batch").agg(
        Azucares_Promedio=("Azúcares Residuales (%)", "mean"),
        Azucares_Mínimo=("Azúcares Residuales (%)", "min"),
        Azucares_Máximo=("Azúcares Residuales (%)", "max"),
    ).reset_index()
    return summary

# Ejemplo de uso
if __name__ == "__main__":
    # Ruta de ejemplo para un archivo de temperatura vs bacterias
    file_path_temp = "temperatura_bacterias.xlsx"
    expected_columns_temp = ["Temperatura (\u00b0C)", "Recuento de Bacterias (UFC/ml)"]

    is_valid_temp, result_temp = validate_excel(file_path_temp, expected_columns_temp)
    if is_valid_temp:
        summary_temp = process_temperature_bacteria(result_temp)
        print("Estadísticas para Temperatura vs Bacterias:")
        print(summary_temp)
    else:
        print(f"Error: {result_temp}")

    # Ruta de ejemplo para un archivo de azúcares residuales
    file_path_azucares = "azucares_residuales.xlsx"
    expected_columns_azucares = ["Batch", "Día", "Azúcares Residuales (%)"]

    is_valid_azucares, result_azucares = validate_excel(file_path_azucares, expected_columns_azucares)
    if is_valid_azucares:
        summary_azucares = process_azucares(result_azucares)
        print("\nEstadísticas para Azúcares Residuales:")
        print(summary_azucares)
    else:
        print(f"Error: {result_azucares}")

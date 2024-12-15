import streamlit as st
from backend.process import validate_excel, process_temperature_bacteria, process_azucares

st.title("Dashboard de Análisis de Datos")

# Selección del tipo de archivo
file_type = st.selectbox("Selecciona el tipo de archivo", ["Temperatura vs Bacterias", "Azúcares Residuales"])

# Subir archivo Excel
uploaded_file = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

if uploaded_file:
    st.write("Procesando archivo...")

    if file_type == "Temperatura vs Bacterias":
        expected_columns = ["Temperatura (°C)", "Recuento de Bacterias (UFC/ml)"]
        is_valid, result = validate_excel(uploaded_file, expected_columns)
        if is_valid:
            st.success("Archivo validado correctamente")
            data = result
            st.write("Datos cargados:")
            st.dataframe(data)

            # Procesar datos
            summary = process_temperature_bacteria(data)
            st.write("Estadísticas descriptivas:")
            for key, stats in summary.items():
                st.write(f"**{key}**")
                st.write(stats)

            # Graficar datos
            st.line_chart(data.set_index("Temperatura (°C)"))
        else:
            st.error(f"Error al procesar el archivo: {result}")

    elif file_type == "Azúcares Residuales":
        expected_columns = ["Batch", "Día", "Azúcares Residuales (%)"]
        is_valid, result = validate_excel(uploaded_file, expected_columns)
        if is_valid:
            st.success("Archivo validado correctamente")
            data = result
            st.write("Datos cargados:")
            st.dataframe(data)

            # Procesar datos
            summary = process_azucares(data)
            st.write("Estadísticas por Batch:")
            st.dataframe(summary)

            # Graficar datos
            st.bar_chart(summary.set_index("Batch"))
        else:
            st.error(f"Error al procesar el archivo: {result}")

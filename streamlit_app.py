# 📅 Cronograma y Dashboard Semanal para CTO

import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
import datetime
import os
from fpdf import FPDF

# ==============================
# Función para registrar avance diario
# ==============================
def registrar_avance(actividad, avance):
    # Verificar si existe el archivo de historial
    if not os.path.exists('historial_avance.csv'):
        with open('historial_avance.csv', 'w') as f:
            f.write('Fecha,Actividad,Avance (%)\n')

    # Registrar avance en el historial
    fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
    with open('historial_avance.csv', 'a') as f:
        f.write(f'{fecha_actual},{actividad},{avance}\n')


# ==============================
# Función para exportar a Excel
# ==============================
def exportar_a_excel(dataframe):
    archivo_excel = 'Reporte_Avance_Semanal.xlsx'
    dataframe.to_excel(archivo_excel, index=False)
    print(f'Reporte exportado a {archivo_excel}')


# ==============================
# Función para exportar a PDF
# ==============================
def exportar_a_pdf(dataframe):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Reporte de Avance Semanal', 0, 1, 'C')

    pdf.set_font('Arial', '', 12)
    for index, row in dataframe.iterrows():
        pdf.cell(0, 10, f"{row['Día']} - {row['Actividad']} - Avance: {row['Avance (%)']}%", 0, 1)

    archivo_pdf = 'Reporte_Avance_Semanal.pdf'
    pdf.output(archivo_pdf)
    print(f'Reporte exportado a {archivo_pdf}')


# Configuración del cronograma
actividades = [
    {'Día': 'Lunes', 'Actividad': 'Revisión de planificación semanal', 'Objetivo': 'Alinear roadmap y recursos estratégicos'},
    {'Día': 'Lunes', 'Actividad': 'Actualización del roadmap estratégico', 'Objetivo': 'Evaluar avances y prioridades de proyectos clave'},
    {'Día': 'Lunes', 'Actividad': 'Revisión de métricas clave', 'Objetivo': 'Monitorear KPIs y ajustar estrategias'},
    {'Día': 'Martes', 'Actividad': 'Revisión de nuevas tecnologías', 'Objetivo': 'Identificar oportunidades de mejora tecnológica'},
    {'Día': 'Martes', 'Actividad': 'Evaluar integraciones con nuevas plataformas', 'Objetivo': 'Optimizar sistemas actuales y futuros'},
    {'Día': 'Martes', 'Actividad': 'Prototipos y PoCs', 'Objetivo': 'Asegurar viabilidad de nuevas iniciativas'},
    {'Día': 'Miércoles', 'Actividad': 'Revisión de incidencias críticas', 'Objetivo': 'Monitorear incidentes y planes de mitigación'},
    {'Día': 'Miércoles', 'Actividad': 'Reuniones con líderes operativos', 'Objetivo': 'Alinear procesos operativos y rendimiento'},
    {'Día': 'Miércoles', 'Actividad': 'Optimización de procesos operativos', 'Objetivo': 'Mejora continua de servicios críticos'},
    {'Día': 'Jueves', 'Actividad': 'Revisión de convocatorias de personal', 'Objetivo': 'Asegurar contratación eficiente y oportuna'},
    {'Día': 'Jueves', 'Actividad': 'Feedback con líderes clave', 'Objetivo': 'Mejora en la gestión de equipos'},
    {'Día': 'Jueves', 'Actividad': 'Coordinación interáreas', 'Objetivo': 'Alineación estratégica con Marketing, Comercial, etc.'},
    {'Día': 'Viernes', 'Actividad': 'Consolidación de informes semanales', 'Objetivo': 'Preparar presentaciones para alta dirección'},
    {'Día': 'Viernes', 'Actividad': 'Identificación de cuellos de botella', 'Objetivo': 'Detección y resolución de problemas'},
    {'Día': 'Viernes', 'Actividad': 'Planificación de la próxima semana', 'Objetivo': 'Preparar actividades a corto plazo'},
]

# Convertir a DataFrame
cronograma_df = pd.DataFrame(actividades)

# Mostrar cronograma
import ace_tools as tools; tools.display_dataframe_to_user(name="Cronograma Semanal para CTO", dataframe=cronograma_df)

# ===========================
# Dashboard de Control Semanal
# ===========================

# Simulación de avance semanal
avance = [75, 60, 70, 85, 90, 50, 80, 70, 65, 60, 75, 80, 70, 80, 90]

cronograma_df['Avance (%)'] = avance

# Mostrar cronograma con avances
tools.display_dataframe_to_user(name="Cronograma con Avance Semanal", dataframe=cronograma_df)

# Gráfico de avance semanal
plt.figure(figsize=(12, 6))
plt.bar(cronograma_df['Actividad'], cronograma_df['Avance (%)'], color='skyblue')
plt.title('Avance Semanal por Actividad')
plt.xlabel('Actividades')
plt.ylabel('Porcentaje de Avance (%)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# ==============================
# Función para mostrar historial
# ==============================
def mostrar_historial():
    if os.path.exists('historial_avance.csv'):
        historial_df = pd.read_csv('historial_avance.csv')
        tools.display_dataframe_to_user(name="Historial de Avances", dataframe=historial_df)
    else:
        print("No se encontró el archivo de historial. Registre al menos un avance para crearlo.")

# Ejemplo de uso:
registrar_avance('Revisión de planificación semanal', 80)
mostrar_historial()

# Exportar a Excel y PDF
exportar_a_excel(cronograma_df)
exportar_a_pdf(cronograma_df)

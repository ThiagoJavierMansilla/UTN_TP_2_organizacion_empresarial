import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos con ruta relativa (Criterio de Reproducibilidad)
df = pd.read_csv('datos/dataset.csv')

# Procesamiento de indicadores del Escenario B
ventas_totales = df['sales amount'].sum()
df['mes'] = df['sales_date'].str[0:7]
ventas_por_mes = df.groupby('mes')['sales amount'].sum()

print(f"--- REPORTE EMITIDO ---")
print(f"Ventas Totales Históricas: ${ventas_totales}\n")
print("Desempeño Comercial Mensual:")
print(ventas_por_mes)

# Generación del gráfico estadístico de evolución
plt.figure(figsize=(6,4))
plt.plot(ventas_por_mes.index, ventas_por_mes.values, marker='o', color='royalblue', linewidth=2)
plt.title('Evolución Mensual de Ventas - Análisis Empresarial')
plt.xlabel('Periodo (Mes)')
plt.ylabel('Monto Facturado ($)')
plt.grid(True)

# Guardado del gráfico en la carpeta de resultados (ruta relativa)
plt.savefig('resultados/grafico_resultados.png')
print("\n[PROCESO EXITOSO]: Gráfico exportado a /resultados/grafico_resultados.png")

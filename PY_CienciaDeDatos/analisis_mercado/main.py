from analysis import analisis_datos_accion, mostrar_analisis, exportar_a_csv

symbol = 'IBM'
df = analisis_datos_accion(symbol)

if df is not None:
    mostrar_analisis(df, symbol)
    exportar_a_csv(df, symbol)
    
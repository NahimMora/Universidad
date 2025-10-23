from analysis import analisis_datos_accion, mostrar_analisis

symbol = 'IBM'
df = analisis_datos_accion(symbol)
mostrar_analisis(df, symbol)
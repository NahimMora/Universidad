# main.py o tu script principal

symbol = 'AAPL'

# 1. Obtener y preparar datos
df = obtener_datos_accion(symbol)

# 2. Calcular métricas
df = calcular_retornos(df)
df = calcular_medias_moviles(df)

# 3. Análisis
print(f"\n=== ANÁLISIS DE {symbol} ===")
analisis_descriptivo(df, symbol)

# 4. Visualizar
graficar_precio_y_volumen(df, symbol)

# 5. (Opcional) Comparar múltiples acciones
comparar_acciones(['AAPL', 'MSFT', 'GOOGL'])
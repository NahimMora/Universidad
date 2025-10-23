import pandas as pd
from data_fetcher import obtener_datos_acciones

def analisis_datos_accion(symbol):
    
    data = obtener_datos_acciones(symbol)
    
    if data is None:
        print(f"Error: No se obtubieron datos para el analisis, data: {data}")
        return None
    
    df = pd.DataFrame(data).T
    
    df.rename(columns={
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. volume': 'volume'
    }, inplace=True)
    
    df = df.astype(float)
    
    df.index = pd.to_datetime(df.index)
    
    df = df.sort_index()
    
    return df
    
def calcular_retornos(df):
    """
        RETORNO: [retorno_diario, retorno_acumulado]
    """
    retorno_diario = ((df['close'] - df['close'].shift(1)) / df['close'].shift(1))* 100
    
    retorno_acumulado = ((1 + df['close'].pct_change()).cumprod() - 1) * 100
    
    retorno_diario = retorno_diario.fillna(0)
    retorno_acumulado = retorno_acumulado.fillna(0)
    
    return retorno_diario, retorno_acumulado
    
    
def analisis_descriptivo(df):
    """
        RETORNO: [precio_max, precio_min, volumen_promedio, cambio_porcentual]
    """
    precio_max = df['close'].max()
    precio_min = df['close'].min()
    
    cambio_porcentual = ((df['close'].iloc[-1] - df['close'].iloc[0]) / df['close'].iloc[0] * 100)
    
    volumen_promedio = df['volume'].mean()
    
    return precio_max, precio_min, volumen_promedio, cambio_porcentual

def mostrar_analisis(df, symbol):
    """
        TODO: Muestra de forma legible el analisis.
    """
    if df is None or df.empty:
        print(f"Error: No hay datos para analizar de {symbol}")
        return
    
    p_max, p_min, vol_prom, cambio = analisis_descriptivo(df)
    
    ret_diario, ret_acum = calcular_retornos(symbol)
    
    print(f"\n{'='*50}")
    print(f"📊 ANÁLISIS DE {symbol}")
    print(f"{'='*50}")
    print(f"Cambio total:      {cambio:+.2f}%")
    print(f"Precio máximo:     ${p_max:.2f}")
    print(f"Precio mínimo:     ${p_min:.2f}")
    print(f"Volumen promedio:  {vol_prom:,.0f}")
    print(f"Volatilidad:       {ret_diario.std():.2f}%")
    print(f"Retorno acumulado: {ret_acum.iloc[-1]:.2f}%")
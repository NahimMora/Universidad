import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

def obtener_datos_acciones(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'Time Series (Daily)' not in data:
            print(f"Error API: {data.get('Note') or data.get('Error Message' , 'Sin datos')}")
            return None
        
        return data['Time Series (Daily)']
    
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")   
        return None
    
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None    
import requests
import csv

def obtener_localidad_por_codigo_postal(codigo_postal):
    url = f"http://api.zippopotam.us/MX/{codigo_postal}"
    #url = f"https://api-sepomex.hckdrk.mx/query/info_cp/{codigo_postal}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "places" in data and len(data["places"]) > 0:
            localidad = data["places"][0]["place name"]
            return localidad
        else:
            return "Localidad no encontrada"
    except Exception as e:
        return f"Error: {str(e)}"

def agregar_localidades_a_csv(entrada_csv, salida_csv):
    with open(entrada_csv, 'r') as archivo_entrada, open(salida_csv, 'w', newline='') as archivo_salida:
        lector_csv = csv.reader(archivo_entrada)
        escritor_csv = csv.writer(archivo_salida)
        
        for fila in lector_csv:
            codigo_postal = fila[0]
            localidad = obtener_localidad_por_codigo_postal(codigo_postal)
            fila.append(localidad)
            escritor_csv.writerow(fila)

entrada_csv = 'cp.csv'  # Cambia esto al nombre de tu archivo CSV de entrada
salida_csv = 'codigos_con_municipio.csv'  # Nombre del archivo CSV de salida

agregar_localidades_a_csv(entrada_csv, salida_csv)
print(f"Localidades agregadas y guardadas en {salida_csv}")

import requests
import csv

def obtener_municipio_por_codigo_postal(codigo_postal):
    url = f"https://snim-api.herokuapp.com/api/v1/consulta_rango_cp/{codigo_postal}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "municipio" in data:
            municipio = data["municipio"]
            return municipio
        else:
            return "Municipio no encontrado"
    except Exception as e:
        return f"Error: {str(e)}"

def agregar_municipios_a_csv(entrada_csv, salida_csv):
    with open(entrada_csv, 'r') as archivo_entrada, open(salida_csv, 'w', newline='', encoding='utf-8') as archivo_salida:
        lector_csv = csv.reader(archivo_entrada)
        escritor_csv = csv.writer(archivo_salida)
        
        for fila in lector_csv:
            codigo_postal = fila[0]
            municipio = obtener_municipio_por_codigo_postal(codigo_postal)
            fila.append(municipio)
            escritor_csv.writerow(fila)

entrada_csv = 'cp.csv'  # Cambia esto al nombre de tu archivo CSV de entrada
salida_csv = 'codigos_con_municipio.csv'  # Nombre del archivo CSV de salida

agregar_municipios_a_csv(entrada_csv, salida_csv)
print(f"Municipios agregados y guardados en {salida_csv}")

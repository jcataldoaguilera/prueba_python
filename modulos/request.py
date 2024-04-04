# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-02
# RLAB-23-02-09-0044-2
#

# Librerias
import requests
import json

# Funciones
def request_get(url):
    return json.loads(requests.get(url).text)

if __name__ == '__main__' :
    # Limitamos la respuesta a 10/216 elementos
    response = request_get('https://aves.ninjas.cl/api/birds')[:10]
    print(response)
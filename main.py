# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-02
# RLAB-23-02-09-0044-2
#

# Librerias
from modulos import html_template as ht
from modulos import card_template as ct
from modulos import request as rq
from modulos import export


# Variables
api = 'https://aves.ninjas.cl/api/birds'
response = rq.request_get('https://aves.ninjas.cl/api/birds')[:10]


# Desarrollo

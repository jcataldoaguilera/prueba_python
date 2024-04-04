# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-02
# RLAB-23-02-09-0044-2
#

# Librerias
from modulos import html_template as ht
from modulos import request as rq
from modulos import export as go


# Variables
response = rq.request_get('https://aves.ninjas.cl/api/birds')
payload_card = ""

# Desarrollo
for d in response :
    payload_card = payload_card + ht.card.substitute(
        name_es = d['name']['spanish'],
        name_en = d['name']['english'],
        img_large = d['images']['full']
    )

payload_index = ht.index.substitute(card = payload_card)

# Exportar index.html
go.export(payload_index)
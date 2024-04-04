# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-02
# RLAB-23-02-09-0044-2
#

# Librerias
from string import Template

# card template
card = Template ('''
                <div class="card" style="width: 18rem;">
                    <img src=$img_large class="card-img-top" alt="$name_en">
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">Nombre: $name_es</li>
                        <li class="list-group-item">Name: $name_en</li>
                    </ul>
                </div>
                '''
                )

if __name__ == '__main__' :
    prueba = card.substitute(img_large = 'foto-grande.jpg', name_es = 'Carpintero', name_en = 'Woodpicker')
    print(prueba)
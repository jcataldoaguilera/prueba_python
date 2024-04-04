# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-02
# RLAB-23-02-09-0044-2
#

# Funciones
def export(var, file):
    with open(file, 'w') as f:
        f.write(var)


if __name__ == '__main__':
    prueba = "hola mundo"
    export(prueba, 'test.html')
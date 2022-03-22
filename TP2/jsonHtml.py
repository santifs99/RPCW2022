import json as json

#Variables
puntPelis = 1
#Creamos diccionarios
peliculasHTML = {}
actores = {}

peliculas = {}
#Creamos arrays tambien
pelisArray = []

#Abrimos el fichero
with open('cinemaATP.json', encoding='utf-8') as ficheroJSON:
    data = json.load(ficheroJSON) #metemos el fichero en data



#Recorremos el dataset y metemos los actores en su diccionario 
#y las peliculas en un array para gestionarlo más tarde
for d in data:
    pelisArray.append(d['title'])
    for actor in d['cast']:
        if actor in actores:
            actores[actor].append(d['title'])
        else:
            actores[actor] = [d['title']]

pelisArray.sort()

#Recorremos el array de peliculas 
for peli in pelisArray:
    peliculasHTML[peli] = puntPelis
    puntPelis+=1


for peli in data:
    peliculas[peli['title']] = peli['year']


#Ordenamos los diccionarios
peliculas = dict(sorted(peliculas.items(), key = lambda x : x[0].lower()))
actores = dict(sorted(actores.items(), key = lambda x : x[0]))

#Definimos metodos que van a crear el HTML
def paginaInicio():
    pagina = open("./paginas/index.html", "w")
    pagina.write('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <title>¡Bienvenido! Lista de peliculas.</title>
    </head>
    <body>''')
    pagina.write("\t\t<div class=\"w3-top\">\n")
    pagina.write("\t\t\t<div class=\"w3-bar w3-black intronav\">\n")
    pagina.write("\t\t\t\t<header>\n")
    pagina.write("\t\t\t\t\t <a href=\"http://localhost:7777/peliculas\" class=\"w3-bar-item w3-button w3-hover-black w3-text-white w3-hover-text-white w3-xlarge\">Filmes</a>\n")
    pagina.write("\t\t\t\t\t <a href=\"http://localhost:7777/actores\" class=\"w3-bar-item w3-button w3-hover-black w3-text-white w3-hover-text-white w3-xlarge\">Atores</a>\n")
    pagina.write("\t\t\t\t</header>\n")
    pagina.write("\t\t\t</div>\n")
    pagina.write("\t\t</div>\n")

    pagina.write('''<div class="w3-container w3-black w3-text-white w3-display-middle">    
            <h1><a href="http://localhost:7777/peliculas">Peliculas</a></h1>
            <h1><a href=\"http://localhost:7777/actores">Actores</a></h1>
        </div>
    </body>
</html>''')

def paginaPeliculas(peliculas):
    pagina = open("./html/filmes.html", "w")
    pagina.write('''<!DOCTYPE html>
<html>
    <head>
        <title> Peliculas </title>  
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    </head>
    <body>''')

    pagina.write("\t\t<div class=\"w3-top\">\n")
    pagina.write("\t\t\t<div class=\"w3-bar w3-black intronav\">\n")
    pagina.write("\t\t\t\t<header>\n")
    pagina.write("\t\t\t\t\t <a href=\"http://localhost:7777/peliculas\" class=\"w3-bar-item w3-button w3-hover-black w3-text-white w3-hover-text-white w3-xlarge\">Filmes</a>\n")
    pagina.write("\t\t\t\t\t <a href=\"http://localhost:7777/actores\" class=\"w3-bar-item w3-button w3-hover-black w3-text-white w3-hover-text-white w3-xlarge\">Atores</a>\n")
    pagina.write("\t\t\t\t</header>\n")
    pagina.write("\t\t\t</div>\n")
    pagina.write("\t\t</div>\n")

    pagina.write("\t\t<div class=\"w3-container w3-black w3-text-white w3-display-middle\">\n")
    pagina.write("\t\t\t<h1><a href=\"http://localhost:7777/peliculas\">Peliculas</a></h1>\n")
    pagina.write("\t\t\t<h1><a href=\"http://localhost:7777/actores\">Actores</a></h1>\n")
    pagina.write("\t\t</div>\n")

    pagina.write("\t</body>\n")

    pagina.write("</html>\n")


def paginaPelicula(peli):
    nombre = str(peliculasHTML.get(peli['title']))
    pagina = open("paginas/peliculas/"+ nombre + ".html", "w")
    pagina.write(f'''<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <title>{peli['title']}</title>
    </head>
    <body>
        <div class="w3-container w3-padding-16">
            <div class="w3-container">
                <h1 class="w3-center w3-blue w3-padding-32 w3-text-black"><b>{peli['title']}</b></h1>
                <ul class="w3-ul w3-card-0 w3-hoverable">
                    <li class="w3-padding-medium"><b>Anio</b>: {peli['year']}</li>
                    <li class="w3-padding-medium"><b>Elenco</b>:
                        <ul class="w3-ul w3-card-0 w3-hoverable">
                        ''')
    for actor in peli['cast']:
        pagina.write("\t\t\t\t<li><a href=\"http://localhost:7777/atores/a" + str(actores.get(actor)) + "\">" + str(actor) + "</a></li>\n")
    pagina.write(f'''</ul>
                    </li>
                    <li class="w3-padding-medium"><b>Género</b>:
                        <ul class="w3-ul w3-card-0 w3-hoverable">
                        ''')
    for genero in peli['genres']:
        pagina.write(f'''\t<li class="w3-padding-medium">{genero}</li>\n\t\t\t\t\t\t''')
    pagina.write(f'''</ul>
                    </li>
                </ul>
                <hr>
                <a href="http://localhost:7777/filmes" class="w3-button w3-blue w3-border-black">Volver a lista de peliculas</a>
            </div>
        </div>
    </body>
</html>''')

def paginaActores(actores):
    pagina = open("paginas/actores/index.html", "w")
    pagina.write(f'''<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <title>Lista de Atores</title>
    </head>
    <body>
        <div class="w3-container w3-padding-16">
            <div class="w3-container">
                <h1 class="w3-center w3-blue w3-padding-32 w3-text-black"><b>Lista de Atores</b></h1>
                <ul class="w3-ul w3-card-0 w3-hoverable">
                ''')
    for actor in actores:
         pagina.write(f'''\t<li class="w3-padding-medium"><a href="http://localhost:7777/atores/{actores[actor]['id']}">{actor}</a></li>\n\t\t\t\t''')
    pagina.write(f'''</ul>
            </div>
        </div>
    </body>
</html>''')

#Creamos la pagina de inicio
paginaInicio()

#Creamos pagina para todas las peliculas
paginaPeliculas(peliculas)

#Creamos la pagina para los actores
#paginaActores(actores)

#Generamos pagina por cada pelicula
for peli in data:
    paginaPelicula(peli)
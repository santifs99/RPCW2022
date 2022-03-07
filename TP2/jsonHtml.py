import json as json

#Abrimos el fichero
with open("cinemaATP.json", encoding='utf-8') as f:
    data = json.load(f) #metemos el fichero en data

for d in data:
    pelicula = open("./html/")

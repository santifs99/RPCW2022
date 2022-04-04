var http = require("http")
var url = require("url")
var fs = require("fs")

function paginaPrincipal() {
    var pargina =
    '<!DOCTYPE html>' +
    '<html lang="es">' +
    '   <head>' +
    '       <meta charset="UTF-8">' +
    '       <meta name="description" content="Información sobre alumnos, intrumentos y cursos">'
    '       <title>Pagina principal</title>' +       
    '       <meta name="viewport" content="width=device-width, initial-scale=1"> ' +
    '       <link rel="stylesheet" href="/estilo.css">' +
    '   </head>' +
    '   <body>' +
    '       <h1>Escola de Música</h1>' +
    '       <ul>' +
    '           <li><a href="http://localhost:4000/alumnos">Listado de alumnos</a></li>' +
    '           <li><a href="http://localhost:4000/instrumentos">Listado de instrumentos</li>' +
    '           <li><a href="http://localhost:4000/cursos">Listado de cursos</a></li>' +
    '       </ul>' +
    '   </body>' +
    '</html>';

    return pargina;
}


function generarTablas() {
    
}
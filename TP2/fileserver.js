var http = require("http")
var url = require("url")
var fs = require("fs")

myserver = http.createServer( function(req,res) {
    
    var miUrl = url.parse(req.url,true).pathname   //cogemos nuestra URL 
    console.log(miUrl);
    var fichero = miUrl.substring(1)  //cogemos el string indicado
    var partes = miUrl.split("/")   //lo separamos  cada vez que haya una /
    
    switch(partes[1]) {
        case 'peliculas':
            if(partes.length==2){
                fichero='peliculas.html'
            }else{
                fichero=partes[2]+".html"
            }
            break;
        case 'actores':
            if(partes.length==2){
                fichero='actores.html'
            }else{
                fichero=partes[2]+".html"
            }
            break;
        default:
            fichero='index.html'
            break;
    }


    
    console.log("Fichero seleccionado " + fichero)
    fs.readFile(fichero , function(err,data){
        res.writeHead(200, {"Content-Type": "text/html; text/css; application/javascript"})
        if(err){
            res.write("<p>Error: no se encontró. </p>")
        }
        else{
            res.write(data)
        }
        res.end()
    })
})

myserver.listen(8888)
console.log("Server funcionando en 8888")
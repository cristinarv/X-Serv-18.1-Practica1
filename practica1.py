#!/usr/bin/python3
# Cristina del Río Vergel
# Práctica 1 (Ejercicio 18.1): Web acortadora de URLs


import webapp
from urllib.parse import unquote


class AcortarUrls (webapp.webApp):

    urls_orig = {}  # Diccionario para poder guardar urls originales
    urls_cortas = {}  # Diccionario para poder guardar urls acortadas

    def parse(self, request):
        return(request.split(' ', 1)[0],
               request.split(' ', 2)[1],
               request.split('=')[-1])

    def process(self, parsedRequest):
        metodo, recurso, body = parsedRequest
        self.urlsCont = len(self.urls_orig)
        if metodo == "GET":
            if recurso == "/":
                return("200 OK", "<html><body>" +
                       """<form action="" method="POST">
                       Introduce una url para acortarla:
                       <input type="text" name="url">
                       <input type="submit" value="Enviar">
                       </form>""" + "Las URLs acortadas que tengo son: " +
                       str(self.urls_cortas) + "</body></html>")
            else:
                recurso = int(recurso[1:])
                if recurso in self.urls_cortas:
                    return("302 Redirect",
                           "<html><head><meta http-equiv='Refresh'" +
                           "content= 4;url=" + self.urls_cortas[recurso] +
                           "/></head" + "<body>Se esta redirigiendo a " +
                           self.urls_cortas[recurso] +
                           "></p></body></html>")
                else:
                    return("404 Not Found",
                           "<html><body><h1>Resource not Found" +
                           "</h1></body></html>")
        elif metodo == "POST":
            if body == "":  # Si no hay nada
                return("404 Not Found",
                       "<html><body><h1>Formulario vacio, meta una url" +
                       "</h1></body></html>")
            else:
                if (body[0:13] == "http%3A%2F%2F" or
                        body[0:14] == "https%3A%2F%2F"):
                    body = unquote(body)
                else:
                    body = "http://" + body  # Ponemos una cabecera
                if body in self.urls_orig:  # Cuando la url ya existe
                    url = ("http://localhost:1234/" +
                           str(self.urls_orig[body]))
                    return("200 Ok",
                           "<html><body>La url acortada que tengo es: " +
                           "<a href=" + url + ">" + url +
                           "</a><br/>La url original que tengo es: <a href=" +
                           body + ">" + body +
                           "</a></body></html>")
                else:  # Cuando la url es nueva
                    self.urls_orig[body] = self.urlsCont
                    url = "http://localhost:1234/" + str(self.urlsCont)
                    self.urls_cortas[self.urlsCont] = body
                    self.urlsCont = self.urlsCont + 1
                    return("200 Ok", "<html><body>" +
                           "<a href=" + url + ">" +
                           url + "</a>" + "</body></html>")
        else:
            return("405 Method Not Allowed", "<html><body><h1>" +
                   "Error: Este metodo no es GET ni POST</h1></body></html>")
if __name__ == "__main__":
    try:
        testWebApp = AcortarUrls("localhost", 1234)
    except KeyboardInterrupt:
        print("Closing binded socket")

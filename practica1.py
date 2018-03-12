#!/usr/bin/python3
import webapp
class webApp (webapp.webApp):
    tightUrls = {}
    completlyUrls = {}
    def parse(self, request):
        return (request.split(' ', 1)[0], 
				request.split(' ', 2)[1],
				request.split('=')[-1])
	
    def process(self, parsedRequest):
        method, recurso, information = parsedRequest 
        self.contador = len(self.completlyUrls)
        if method =="GET":
            if recurso =="/":
                returnCode = "HTTP/1.1 200 OK"
                htmlAnswer = ("<html><body>" + "<form method = 'POST'>" + "La URL que se quiere acortar es: " + "<input type='text' name='url'><br>" +
                              "<input type='submit' value='Acorta la url'></form>" + str(self.tightUrls) + "</body></html>")
            else:
                recurso = int(recurso[1:])
                if recurso in self.tightUrls:
                    returnCode = "HTTP/1.1 302 Found"
                    htmlAnswer = ("<html><body><meta http-equiv='refresh'" + "information='1 url=" +
                                self.tightUrls[recurso] + "'>" + "</p>" + "</body></html>")
                else:
                    returnCode = "HTTP/1.1 404 Not Found"
                    htmlAnswer = ("<html><body>" +
                                  "recurso Not FoundR</body></html>"
        if metodo =="POST":
            if body == "":  # Es un formulario vacio
                return("404 Not Found",
                       "<html><body><h1>Formulario vacio, meta una url" +
                       "</h1></body></html>")
            else:
                if (body[0:13] == "http%3A%2F%2F" or
                        body[0:14] == "https%3A%2F%2F"):
                    body = unquote(body)
                else:
                    body = "http://" + body  # Ponemos una cabecera
                if body in self.urls_orig:
                    url_corta = ("http://localhost:1234/" +
                                 str(self.urls_orig[body]))
                    return("200 Ok", "<html><body>La url_corta es:6666666666 " +
                           "<a href=" + url_corta + ">" + url_corta +
                           "</a>" + "</body></html>")
                else:
                    self.urls_orig[body] = self.urlsCont
                    enlace = "http://localhost:1234/" + str(self.urlsCont)
                    self.urls_cortas[self.urlsCont] = body
                    self.urlsCont = self.urlsCont + 1
                    return("HTTP/1.1 200 Ok", "<html><body>" +
                           "<a href=" + enlace + ">" +
                           enlace + "</a>" + "</body></html>")
        else:
            returnCode = "HTTP/1.1 405 Method Not Allowed"
            htmlAnswer = "Method Not Allowed"
        
if __name__ == "__main__":
    testWebApp = webApp("localhost", 1234)

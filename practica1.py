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
        if method == method == "GET":
            if recurso =="/":
                returnCode = "HTTP/1.1 200 OK"
                htmlAnswer = ("<html><body>" + "<form method = 'POST'>" + "La URL que se quiere acortar es: " + "<input type='text' name='url'><br>" +
                              "<input type='submit' value='Acorta la url'></form>" + str(self.tightUrls) + "</body></html>")
            elif recurso == "/favicon.ico":
                 return("404 Not Found",
                        "<html><body><h1>Recurso no encontrado" +
                        "</h1></body></html>")
            else:
                recurso = int(recurso[1:])
                if recurso in self.tightUrls:
                    returnCode = "HTTP/1.1 302 Found"
                    htmlAnswer = ("<html><body><meta http-equiv='refresh'" + "information='1 url=" +
                                self.tightUrls[recurso] + "'>" + "</p>" + "</body></html>")
                else:
                    returnCode = "HTTP/1.1 404 Not Found"
                    htmlAnswer = ("<html><body>" +
                                  "recurso Not FoundR</body></html>")
        else:
            returnCode = "HTTP/1.1 405 Method Not Allowed"
            htmlAnswer = "Method Not Allowed"
        return (returnCode, htmlAnswer)
if __name__ == "__main__":
    testWebApp = webApp("localhost", 1234)

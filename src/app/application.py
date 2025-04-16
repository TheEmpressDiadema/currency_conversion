from http.server import BaseHTTPRequestHandler, HTTPServer

class Application:

    def run(server_class: HTTPServer = HTTPServer,
            handler_class: BaseHTTPRequestHandler = BaseHTTPRequestHandler):
        pass
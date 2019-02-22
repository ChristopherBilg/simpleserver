#!/usr/bin/env python3

import http.server
import socketserver as SocketServer
import os

HOST = ""
PORT = 8000
FILENAME = "client_information.txt"

if os.path.exists(FILENAME):
    os.remove(FILENAME)


class TCPHandler(http.server.SimpleHTTPRequestHandler):
    """
    TCP Handler Class
    """
    def do_GET(self):
        """
        Overwritten do_GET() method to respond to GET requests.
        """
        if self.path == "/" or self.path == "":
            self.path = "/index.html"

        with open(FILENAME, "a+") as textfile:
            textfile.write(str(self.headers))

        return http.server.SimpleHTTPRequestHandler.do_GET(self)


with SocketServer.TCPServer((HOST, PORT), TCPHandler) as httpd:
    print("Serving at port " + str(PORT))
    httpd.serve_forever()

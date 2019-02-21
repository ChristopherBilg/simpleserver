#!/usr/bin/env python3

import http.server
import socketserver

HOST = ""
PORT = 8000
HANDLER = http.server.SimpleHTTPRequestHandler


class MyTCPHandler(http.server.SimpleHTTPRequestHandler):
    """
    dsfds
    """
    def handle(self):
        """
        sadas
        """
        self.data = self.request.recv(1024).strip()
        print(self.data)


with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as httpd:
    print("Serving at port " + str(PORT))
    print(str(httpd.get_request()))
    httpd.serve_forever()

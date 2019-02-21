#!/usr/bin/env python3

import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print(str(httpd.get_request()))
    print(str(httpd.server_address))
    httpd.serve_forever()

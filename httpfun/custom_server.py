#!/usr/bin/env python
# custom_server.py
# Micah raabe

# Lab 52 - Construct a SimpleHTTPServer ande HTTP Client

import SimpleHTTPServer
import SocketServer

PORT = 9021

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

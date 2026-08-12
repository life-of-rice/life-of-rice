import os, http.server, socketserver
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 3700
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as h:
    h.serve_forever()

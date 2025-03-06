
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

# Create directory for HTML files if it doesn't exist
os.makedirs('static', exist_ok=True)

# Create the server
server = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
print("Server started at http://0.0.0.0:8080")
server.serve_forever()

from wsgiref.simple_server import make_server

from hello import app
httpd = make_server('', 8000, app)
httpd.serve_forever()
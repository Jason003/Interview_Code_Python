def app(environ, response):
	response('200 OK', [('Content-Type', 'text/html')])
	return [b'<h1>Hello, world!</h1>']

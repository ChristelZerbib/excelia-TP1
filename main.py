from bottle import route, run, template


@route('/')
def index():
    return "Hello World!"

run(host='localhost', port=8085)


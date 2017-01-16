from gevent.wsgi import WSGIServer

from app.common.factory import create_app

app = create_app('bs_flask')

if __name__ == '__main__':
    # start WSGI http server as undefined host
    http_server = WSGIServer(('', 80), app)
    http_server.serve_forever()

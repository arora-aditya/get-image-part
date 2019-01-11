import tornado.ioloop
import tornado.web
import tornado.wsgi
import io
import time
import random
import os
from wsgiref.simple_server import make_server, WSGIServer
from SocketServer import ThreadingMixIn

from PIL import Image
N = 20

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(random.uniform(0,N))
        img = int(self.get_argument("img"))
        fn = os.path.join(os.path.dirname(__file__), "images/"+str(img)+".jpg")
        im = Image.open(fn)
        dim = im.size
        c = im.crop((int(n*dim[0]/N), 0, int((n+1)*dim[0]/N), dim[1]))
        c = c.convert("RGBA")
        bio = io.BytesIO()
        c.save(bio, 'PNG')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Content-Type', 'image/jpeg')
        self.set_header('X-ECE459-Fragment', str(n))
        time.sleep(abs(random.gauss(0.2, 0.2)))
        self.write(bio.getvalue())

class ThreadingWSGIServer(ThreadingMixIn, WSGIServer):
    pass
        
application = tornado.wsgi.WSGIApplication([
    (r"/image", MainHandler),
])

if __name__ == "__main__":
    import logging
    import wsgiref.simple_server

    logger = logging.getLogger('tornado.application')
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    server = wsgiref.simple_server.make_server('', 8000, application, ThreadingWSGIServer)
    server.serve_forever()

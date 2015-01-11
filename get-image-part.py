import tornado.ioloop
import tornado.web
import tornado.wsgi
import io
import time
import random
import os

from PIL import Image
N = 20

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument("n"))
        img = int(self.get_argument("img"))
        fn = os.path.join(os.path.dirname(__file__), "images/"+str(img)+".jpg")
        im = Image.open(fn)
        dim = im.size
        c = im.crop((int(n*dim[0]/N), 0, int((n+1)*dim[0]/N), dim[1]))
        bio = io.BytesIO()
        c.save(bio, 'JPEG')
        self.set_header('Content-Type', 'image/jpeg')
        time.sleep(abs(random.gauss(0.2, 0.2)))
        self.write(bio.getvalue())

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
    server = wsgiref.simple_server.make_server('', 8000, application)
    server.serve_forever()

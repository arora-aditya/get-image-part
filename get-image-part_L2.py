#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import tornado.wsgi
import io
import time
import random
import os

from tornado.log import enable_pretty_logging
from PIL import Image
N = 50

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(random.uniform(0,N))
        img = int(self.get_argument("img"))
        fn = os.path.join(os.path.dirname(__file__), "images/"+str(img)+"/output_"+str(n)+".png")
        im = Image.open(fn)
        dim = im.size
        c = im.convert("RGBA")
        bio = io.BytesIO()
        c.save(bio, 'PNG')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Content-Type', 'image/jpeg')
        self.set_header('X-Ece252-Fragment', str(n))
        time.sleep(abs(random.gauss(0.2, 0.2)))
        self.write(bio.getvalue())

application = tornado.web.Application([
    (r"/image", MainHandler),
])

if __name__ == "__main__":
    import logging

    logger = logging.getLogger('tornado.application')
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    application.listen(2520)
    enable_pretty_logging()
    tornado.ioloop.IOLoop.instance().start()

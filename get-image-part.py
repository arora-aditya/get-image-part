import tornado.ioloop
import tornado.web
import io
import time
import random

from PIL import Image
N = 20

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument("n"))
        img = int(self.get_argument("img"))
        im = Image.open("images/"+str(img)+".jpg")
        dim = im.size
        c = im.crop((n*dim[0]/N, 0, (n+1)*dim[0]/N, dim[1]))
        bio = io.BytesIO()
        c.save(bio, 'JPEG')
        self.set_header('Content-Type', 'image/jpeg')
        time.sleep(abs(random.gauss(0.2, 0.2)))
        self.write(bio.getvalue())

application = tornado.web.Application([
    (r"/image", MainHandler),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

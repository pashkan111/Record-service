import tornado.ioloop
import tornado.web


def make_app():
    return tornado.web.Application([])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
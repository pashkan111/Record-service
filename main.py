import tornado.ioloop
import tornado.web
from src.service_app import Base
from db.db import engine


def make_app():
    Base.metadata.create_all(engine)
    return tornado.web.Application([])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
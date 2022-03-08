import tornado.ioloop
import tornado.web
from src.service_app import Base
from db.db import engine
from src.service_app.routes import RecordHandler


def make_app():
    Base.metadata.create_all(engine)
    return tornado.web.Application([
        ('/api/add', RecordHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
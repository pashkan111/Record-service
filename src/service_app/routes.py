from tornado.web import RequestHandler
import json
from .models import Record


class RecordHandler(RequestHandler):
    def post(self):
        data_loaded = json.loads(self.request.body)
        key = Record.add_record(data_loaded)
        self.write({'key': key})

        
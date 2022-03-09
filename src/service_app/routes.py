from tornado.web import RequestHandler
import json
from .models import Record
# from .services import sqlalchemy_obj_to_dict
from .schemas import RecordSchema


class RecordPostHandler(RequestHandler):
    def post(self):
        data_loaded = json.loads(self.request.body)
        key = Record.add_record(data_loaded)
        self.write({'key': key})


class RecordGetHandler(RequestHandler):
    def get(self):
        key = self.get_argument('key')
        if key:
            record = Record.get_record_by_key(key)
            record_loaded = RecordSchema.from_orm(record).dict()
            self.write(record_loaded)
        else:
            self.write({'key': 'None'})
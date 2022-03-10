from tornado.web import RequestHandler
import json
from .models import Record
import pydantic
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
            try:
                record_loaded = RecordSchema.from_orm(record).dict()
                self.write(record_loaded)
            except pydantic.error_wrappers.ValidationError:
                self.write({'message': 'Record with such key does not exist'})
        else:
            self.write({'message': 'The key is required!'})
            
            
class RecordRemoveHandler(RequestHandler):
    def delete(self):
        key = self.get_argument('key')
        if key:
            try:
                Record.delete_record_by_key(key)
                self.write({'message': "The record successfully deleted"})
            except:
                self.write({'message': 'Record with such key does not exist'})
        else:
            self.write({'message': 'The key is required!'})
            
import sqlalchemy as sa
from db.db import Base, session
from sqlalchemy.dialects.postgresql import JSON
from .services import create_base64_key
import json


class Record(Base):
    __tablename__ = 'record'
    id = sa.Column(sa.Integer, primary_key=True)
    key = sa.Column(sa.String(64))
    data = sa.Column(JSON)
    count = sa.Column(sa.Integer, default=0)
    
    @classmethod
    def add_record(cls, data: json) -> str:
        key = create_base64_key(data)
        new_record = cls(key=key, data=data)
        session.add(new_record)
        session.commit()
        return key
    
    @classmethod
    def get_record_by_key(cls, key: str):
        record = session.query(cls).filter(cls.key==key).first()
        return record
    
import sqlalchemy as sa
from db.db import Base, session
from sqlalchemy.dialects.postgresql import JSON
from .services import create_base64_key
import json
from sqlalchemy.orm.exc import NoResultFound


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
    
    @classmethod
    def delete_record_by_key(cls, key: str):
        record = session.query(cls).filter(cls.key==key).first()
        if not record:
            raise NoResultFound
        session.delete(record)
        session.commit()
        session.close()
        
    @classmethod
    def update_record(cls, key: str, data: dict):
        record = session.query(cls).filter(cls.key==key).first()
        if not record:
            raise NoResultFound
        record.data = data
        record.count = 0
        session.add(record)
        session.commit()
        return record
        
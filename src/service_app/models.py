import sqlalchemy as sa
from db.db import Base, session
from sqlalchemy.dialects.postgresql import JSON
from .schemas import DataPostSchema
from services import create_base64_key


class Record(Base):
    __tablename__ = 'record'
    id = sa.Column(sa.Integer, primary_key=True)
    key = sa.Column(sa.String(64))
    data = sa.Column(JSON)
    
    @classmethod
    def add_record(cls, data: DataPostSchema) -> str:
        key = create_base64_key(data)
        new_record = cls(key=key, data=data)
        session.add(new_record)
        session.commit()
        return key
    
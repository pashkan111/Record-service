import sqlalchemy as sa
from db.db import Base, session
from sqlalchemy.dialects.postgresql import JSON
from .schemas import DataPostSchema


class Data(Base):
    __tablename__ = 'data'
    id = sa.Column(sa.Integer, primary_key=True)
    key = sa.Column(sa.String(64))
    data = sa.Column(JSON)
    
    @classmethod
    def add_data(cls, data: DataPostSchema, key: str) -> str:
        new_record = cls(key=key, data=data)
        session.add(new_record)
        session.commit()
        return key
    
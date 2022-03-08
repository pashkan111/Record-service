import sqlalchemy as sa
from db.db import Base
from sqlalchemy.dialects.postgresql import JSON


class Data(Base):
    __tablename__ = 'data'
    id = sa.Column(sa.Integer, primary_key=True)
    key = sa.Column(sa.String(64))
    data = sa.Column(JSON)
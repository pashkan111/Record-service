import sqlalchemy as sa
from db.db import Base
from sqlalchemy.dialects.postgresql import JSON


class Data(Base):
    __tablename__ = 'data'
    id = sa.Column(sa.String(64), primary_key=True)
    data = sa.Column(JSON)
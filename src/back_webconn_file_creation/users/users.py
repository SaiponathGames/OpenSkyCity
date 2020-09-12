from back_webconn_file_creation.keys.keys import Key
from sqlalchemy import Integer, Sequence, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from ..settings import Settings

settings = Settings()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), autoincrement=True)

    def __init__(self, **data):
        self.id_ = data.pop('id', None)
        self.name = data.pop('name', None)
        self.email = data.pop('email', None)
        self.password = data.pop('password', None)
        self._keys = data.pop('keys', None)

    def add_key(self, key):
        if not self._keys:
            self._keys = []
        self._keys.append(key.id_)

    def remove_key(self, key):
        if not self._keys:
            self._keys = []
        self._keys.remove(key.id_)

    @property
    def keys(self):
        return [Key]

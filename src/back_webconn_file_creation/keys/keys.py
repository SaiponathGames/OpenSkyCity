from back_webconn_file_creation.users.users import User

from ..db_conn import db


class Key(db.Model):
    __tablename__ = 'keys'

    id = db.Column(db.Integer(), primary_key=True)



    def __init__(self, **data):
        self.id_ = data.pop('id', None)
        self._key = data.pop('key', None)
        self.type_ = data.pop('type', None)
        self._user_id = data.pop('owner_id', None)

    @property
    def owner(self):
        return User

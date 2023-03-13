from ..db import ctx_db


class User:
    def __init__(self, uid, email, full_name, auth_level, password):
        self.uid = uid
        self.email = email
        self.full_name = full_name
        self.auth_level = auth_level
        self.password_hash = password

    @staticmethod
    def from_dict(data):
        user = User(data['_id'], data['email'], data['full_name'], data['auth_level'], data['password'])
        return user

    def to_dict(self):
        return {
            'uid': self.uid,
            'email': self.email,
            'full_name': self.full_name,
            'auth_level': self.auth_level,
            'password_hash': self.password_hash
        }

    def to_user_data(self):
        return {
            'uid': self.uid,
            'email': self.email,
            'full_name': self.full_name,
            'auth_level': self.auth_level
        }

    @classmethod
    def find_by_email(cls, email):
        data = ctx_db.users.find_one({'email': email})
        print("data:", data)
        return cls.from_dict(data) if data else None

    def save(self):
        data = self.to_dict()
        ctx_db.users.update_one({'email': self.email}, {'$set': data}, upsert=True)

    def delete(self):
        ctx_db.users.delete_one({'email': self.email})

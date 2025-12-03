from App.database import db
from .user import User

class Admin(User):
    __tablename__ = "admin"

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "Admin",
    }

    def __init__(self, username, password):
        super().__init__(username, password)

    def get_json(self):
        user_json = super().get_json()
        return user_json

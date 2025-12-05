from App.database import db
from .user import User
from .notification import Notification

MAX_INBOX_SIZE = 20


class Resident(User):
    __tablename__ = "resident"

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    areaId = db.Column(db.Integer, db.ForeignKey('area.id'), nullable=False)
    streetId = db.Column(db.Integer,
                         db.ForeignKey('street.id'),
                         nullable=False)
    houseNumber = db.Column(db.Integer, nullable=False)
    inbox = db.relationship("Notification", backref="resident", lazy=True)

    area = db.relationship("Area", backref='residents')
    street = db.relationship("Street", backref='residents')
    stops = db.relationship('Stop', backref='resident')

    __mapper_args__ = {
        "polymorphic_identity": "Resident",
    }

    def __init__(self, username, password, areaId, streetId, houseNumber):
        super().__init__(username, password)
        self.areaId = areaId
        self.streetId = streetId
        self.houseNumber = houseNumber

    def get_json(self):
        user_json = super().get_json()
        user_json['areaId'] = self.areaId
        user_json['streetId'] = self.streetId
        user_json['houseNumber'] = self.houseNumber
        user_json['inbox'] = self.inbox
        return user_json

    def update(self, message: str, driverID=None) -> None:
        """Observer pattern update method - receives notifications from drivers."""
        notif = Notification(resident_id=self.id, message=message, driver_id=driverID)
        if len(self.inbox) >= MAX_INBOX_SIZE:
            oldest_notif = min(self.inbox, key=lambda n: n.date)
            db.session.delete(oldest_notif)
        db.session.add(notif)
        db.session.commit()

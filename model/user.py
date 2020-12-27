from passlib.hash import pbkdf2_sha256

from model.base import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    address = db.relationship("Address", backref=db.backref("user", uselist=False))
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    __mapper_args__ = {
       "polymorphic_identity": __tablename__,
       "polymorphic_on": category,
    }

    def __init__(self, user_name, password, category, phone_number, email):
        self.user_name = user_name
        self.password_hash = self.generate_hash(password)
        self.category = category
        self.phone_number = phone_number
        self.email = email

    @staticmethod
    def generate_hash(password):
        return pbkdf2_sha256.hash(password.encode("utf8"))

    @staticmethod
    def verify_hash(password, hashed_password):
        return pbkdf2_sha256.verify(password.encode("utf8"), hashed_password)

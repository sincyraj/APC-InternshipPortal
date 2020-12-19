from passlib.context import CryptContext

from base import db

PASSLIB_CONTEXT = CryptContext(
    # in a new application with no previous schemes, start with pbkdf2 SHA512
    schemes=["pbkdf2_sha512"],
    deprecated="auto",
)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship("Address", backref=db.backref("user", uselist=False))
    user_name = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "user",
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
        return PASSLIB_CONTEXT.hash(password.encode("utf8"))

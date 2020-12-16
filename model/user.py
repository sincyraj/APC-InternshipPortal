
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from model.base import Base

from passlib.context import CryptContext


PASSLIB_CONTEXT = CryptContext(
    # in a new application with no previous schemes, start with pbkdf2 SHA512
    schemes=["pbkdf2_sha512"],
    deprecated="auto",
)
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(50))
    phone_number = Column(String(50))
    email = Column(String(50))
    address_id = Column(Integer, ForeignKey('address.id'))
    address = relationship("Address", backref=backref("user", uselist=False))
    user_name = Column(String(50), unique=True)
    password_hash = Column(String(256), nullable=False)

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

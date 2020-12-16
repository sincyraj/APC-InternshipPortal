
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from model.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(50))
    phone_number = Column(String(50))
    email = Column(String(50))
    address_id = Column(Integer, ForeignKey('address.id'))
    address = relationship("Address", backref=backref("user", uselist=False))

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": category,
    }

    def __init__(self, category, phone_number, email):
        self.category = category
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return "Ordinary person %s" % self.name

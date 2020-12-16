from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref

from model.user import User


class Student(User):
    __tablename__ = "student"
    id = Column(ForeignKey("user.id"), primary_key=True)
    first_name = Column(String(30))
    middle_name = Column(String(30))
    last_name = Column(String(30))
    registration_id = Column(String(50), unique=True)

    program_id = Column(Integer, ForeignKey('program.id'))
    program = relationship("Program", backref=backref("student", uselist=False))

    __mapper_args__ = {"polymorphic_identity": __tablename__}

    def __init__(self, phone_number, email, first_name, middle_name, last_name, registration_id):
        super().__init__("student", phone_number, email)
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.registration_id = registration_id

    def __repr__(self):
        return (
            "Name %s %s %s, "
            % (
                self.first_name,
                self.middle_name,
                self.last_name
            )
        )
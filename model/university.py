from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from model import university_program
from model.user import User


class University(User):
    __tablename__ = "university"
    id = Column(ForeignKey("user.id"), primary_key=True)
    name = Column(String(150))
    university_code = Column(String(50), unique=True)

    programs = relationship("Program", secondary="university_program", backref="universities")

    __mapper_args__ = {"polymorphic_identity": __tablename__}

    def __init__(self, user_name, password, phone_number, email, name, university_code):
        super().__init__(user_name, password, "university", phone_number, email)
        self.name = name
        self.university_code = university_code

    def __repr__(self):
        return (
                "University Name %s, "
                % (
                    self.name
                )
        )

from base import db
from model.user import User


class University(User):
    __tablename__ = "university"
    id = db.Column(db.ForeignKey("user.id"), primary_key=True)
    name = db.Column(db.String(150))
    university_code = db.Column(db.String(50), unique=True)

    programs = db.relationship("Program", secondary="university_program", backref="universities")

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

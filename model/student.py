from model.base import db

from model.user import User


class Student(User):
    __tablename__ = "student"
    id = db.Column(db.ForeignKey("user.id"), primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    middle_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    registration_id = db.Column(db.String(50), unique=True, nullable=False)

    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=False)
    program = db.relationship("Program", backref=db.backref("student", uselist=False))

    __mapper_args__ = {"polymorphic_identity": __tablename__}

    def __init__(self, user_name, password, phone_number, email, first_name, middle_name, last_name, registration_id):
        super().__init__(user_name, password, "student", phone_number, email)
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.registration_id = registration_id


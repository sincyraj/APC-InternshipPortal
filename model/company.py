from model.base import db
from model.user import User


class Company(User):
    __tablename__ = "company"
    id = db.Column(db.ForeignKey("user.id"), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    __mapper_args__ = {"polymorphic_identity": __tablename__}
    company_code = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, user_name, password, phone_number, email, name, company_code):
        super().__init__(user_name, password, "company", phone_number, email)
        self.name = name
        self.company_code = company_code

    def __repr__(self):
        return "Company %s" % self.name

from model.base import db

class OpenInternship(db.Model):
    __tablename__ = "open_internship"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    internship_code = db.Column(db.String(50), unique=True, nullable=False)

    company_id = db.Column(db.ForeignKey("company.id"), nullable=False)
    company = db.relationship("Company", backref=db.backref("open_internship", uselist=False))

    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(350), nullable=False)
    required_cgpa = db.Column(db.String(30), nullable=False)
    comments = db.Column(db.String(300))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __init__(self, internship_code, company_id, title, description, required_cgpa, comments, start_date, end_date):
        self.internship_code = internship_code
        self.company_id = company_id
        self.title = title
        self.description = description
        self.required_cgpa = required_cgpa
        self.comments = comments
        self.start_date = start_date
        self.end_date = end_date
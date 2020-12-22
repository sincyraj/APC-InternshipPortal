from model.base import db

class Internship(db.Model):
    __tablename__ = "internship"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    internship_code = db.Column(db.String(50), unique=True, nullable=False)

    university_id = db.Column(db.ForeignKey("university.id"), nullable=False)
    university = db.relationship("University", backref=db.backref("internship", uselist=False))

    student_id = db.Column(db.ForeignKey("student.id"), nullable=False)
    student = db.relationship("Student", backref=db.backref("internship", uselist=False))

    company_id = db.Column(db.ForeignKey("company.id"), nullable=False)
    company = db.relationship("Company", backref=db.backref("internship", uselist=False))

    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(350), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    required_cgpa = db.Column(db.String(30), nullable=False)
    comments = db.Column(db.String(300))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __init__(self, internship_code, university_id, student_id, company_id, title, description, status, required_cgpa, comments, start_date, end_date):
        self.internship_code = internship_code
        self.university_id = university_id
        self.student_id = student_id
        self.company_id = company_id
        self.title = title
        self.description = description
        self.status = status
        self.required_cgpa = required_cgpa
        self.comments = comments
        self.start_date = start_date
        self.end_date = end_date
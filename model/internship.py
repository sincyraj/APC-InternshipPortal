from model.base import db

class Internship(db.Model):
    __tablename__ = "internship"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    internship_code = db.Column(db.String(50), unique=True)
    university_id = db.Column(db.ForeignKey("university.id"))
    student_id = db.Column(db.ForeignKey("student.id"))
    company_id = db.Column(db.ForeignKey("company.id"))
    status = db.Column(db.String(30))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    def __init__(self, internship_code, university_id, student_id, company_id, status, start_date, end_date):
        self.internship_code = internship_code
        self.university_id = university_id
        self.student_id = student_id
        self.company_id = company_id
        self.status = status
        self.start_date = start_date
        self.end_date = end_date

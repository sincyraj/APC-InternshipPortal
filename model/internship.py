from model.base import db

class Internship(db.Model):
    __tablename__ = "internship"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    internship_code = db.Column(db.String(50), unique=True)
    university_id = db.Column(db.ForeignKey("university.id"))
    student_id = db.Column(db.ForeignKey("student.id"))
    company_id = db.Column(db.ForeignKey("company.id"))
    title = db.Column(db.String(250))
    description = db.Column(db.String(350))
    status = db.Column(db.String(30))
    required_cgpa = db.Column(db.String(30))
    comments = db.Column(db.String(300))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

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

from model.base import db

class Internship(db.Model):
    __tablename__ = "internship"
    internship_id = db.Column(db.ForeignKey("internship.id"), nullable=False)
    university_id = db.Column(db.ForeignKey("university.id"), nullable=False)
    university = db.relationship("University", backref=db.backref(__tablename__, uselist=False))

    student_id = db.Column(db.ForeignKey("student.id"), nullable=False)
    student = db.relationship("Student", backref=db.backref(__tablename__, uselist=False))
    status = db.Column(db.String(30), nullable=False)

    def __init__(self, internship_code, university_id, student_id, status):
        self.internship_code = internship_code
        self.university_id = university_id
        self.student_id = student_id
        self.status = status
from sqlalchemy import update

from model.base import db
from model.company import Company
from model.internship import Internship
from model.student import Student
from model.university import University


def fetch_all_internships():
    return Internship.query\
        .join(University, Internship.university_id == University.id)\
        .join(Student, Internship.student_id == Student.id)\
        .join(Company, Internship.company_id == Company.id).all()


def update_internships(action, ids):
    for id in ids:
        if action == "approve":
            status = "Approved"
        elif action == "reject":
            status = "Rejected"
        db.session.execute(update(Internship).where(Internship.id == id).values(status=status))
        db.session.commit()
from sqlalchemy import update

from model.base import db
from model.company import Company
from model.open_internship import OpenInternship
from model.student import Student
from model.university import University


def fetch_all_internships():
    return OpenInternship.query\
        .join(University, OpenInternship.university_id == University.id)\
        .join(Student, OpenInternship.student_id == Student.id)\
        .join(Company, OpenInternship.company_id == Company.id).all()


def update_internships(action, ids):
    for id in ids:
        if action == "approve":
            status = "Approved"
        elif action == "reject":
            status = "Rejected"
        db.session.execute(update(OpenInternship).where(OpenInternship.id == id).values(status=status))
        db.session.commit()
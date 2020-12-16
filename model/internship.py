from sqlalchemy import Column, String, ForeignKey, Date, Integer

from model.base import Base


class Internship(Base):
    __tablename__ = "internship"

    id = Column(Integer, primary_key=True, autoincrement=True)

    internship_code = Column(String(50), unique=True)
    university_id = Column(ForeignKey("university.id"))
    student_id = Column(ForeignKey("student.id"))
    company_id = Column(ForeignKey("company.id"))
    status = Column(String(30))
    start_date = Column(Date)
    end_date = Column(Date)

    def __init__(self, internship_code, university_id, student_id, company_id, status, start_date, end_date):
        self.internship_code = internship_code
        self.university_id = university_id
        self.student_id = student_id
        self.company_id = company_id
        self.status = status
        self.start_date = start_date
        self.end_date = end_date

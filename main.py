from datetime import datetime
from model.base import db
from model.address import Address
from model.company import Company
from model.internship import Internship
from model.program import Program
from model.student import Student
from model.university import University

from model.university_program import university_program #Dont remove

db.create_all()
address1 = Address("Distelstraat 6", "Schaerbeek", "Brussels", "Brussels", "Belgium", "1030")
address2 = Address("Hemeryckxlaan 10", "Kontich", "Antwerp", "Antwerp", "Belgium", "2660")
address3 = Address("Uitbreidingstraat 8", "Berchem", "Antwerp", "Antwerp", "Belgium", "2600")

company = Company("uza", "password", "+3212345678", "user@example.com", "UZA", "CPY1")
company.address = address1

program = Program("Masters in Applied Computer Science", "MACS")

student = Student("john.oliver", "password", "+3245678910", "student@uni.be", "John", "Oliver", "Gates", "STU1")
student.address = address2
student.program = program

university = University("ua_uni1", "password", "+32889966771", "admin@uni.be", "UA", "UNI1")
university.address = address3
university.programs.append(program)

db.session.add(address1)
db.session.add(address2)
db.session.add(company)
db.session.add(program)
db.session.add(student)
db.session.add(university)
db.session.commit()

db_student = db.session.query(Student).filter(Student.id == 2).one()
db_university = db.session.query(University).filter(University.id == 3).one()
db_company = db.session.query(Company).filter(Company.id == 1).one()
internship = Internship("INT1", db_university.id, db_student.id, db_company.id, "AVAILABLE", datetime.today(),
                        datetime.today())

db.session.add(internship)
db.session.commit()

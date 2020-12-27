from datetime import datetime
from model.base import db
from model.address import Address
from model.company import Company
from model.internship import Internship
from model.open_internship import OpenInternship
from model.program import Program
from model.student import Student
from model.university import University

from model.university_program import university_program  # Dont remove

db.create_all()
address1 = Address("Distelstraat 6", "Schaerbeek", "Brussels", "Brussels", "Belgium", "1030")
address2 = Address("Hemeryckxlaan 10", "Kontich", "Antwerp", "Antwerp", "Belgium", "2660")
address3 = Address("Uitbreidingstraat 8", "Berchem", "Antwerp", "Antwerp", "Belgium", "2600")
address4 = Address("Celestijnenlaan 69", "", "Leuven", "Vlaams-Brabant", "Belgium", "3000")

company = Company("uza", "password", "+3212345678", "user@example.com", "UZA", "CPY1")
company.address = address1

program = Program("Masters in Applied Computer Science", "MACS")

student1 = Student("student1", "password1", "+3245678910", "stus@uni.be", "Jeff", "Ronald", "Bezos", "STU1")
student1.address = address2
student1.program = program

student2 = Student("student2", "password2", "+3244557766", "stu2@uni.be", "John", "Bill", "Gates", "STU2")
student2.address = address4
student2.program = program

student3 = Student("student3", "password3", "+3244557786", "stu3@uni.be", "Shawn", "James", "Hill", "STU3")
student3.address = address4
student3.program = program

university = University("ua_uni1", "password3", "+32889966771", "admin@uni.be", "UA", "UNI1")
university.address = address3
university.programs.append(program)

db.session.add(address1)
db.session.add(address2)
db.session.add(company)
db.session.add(program)
db.session.add(student1)
db.session.add(student2)
db.session.add(university)
db.session.commit()

db_student1 = db.session.query(Student).filter(Student.registration_id == "STU1").one()
db_university1 = db.session.query(University).filter(University.university_code == "UNI1").one()
db_company1 = db.session.query(Company).filter(Company.company_code == "CPY1").one()

open_internship1 = OpenInternship("INT1", db_company1.id, "My title1", "My Description1", "6.15", "My comments1", datetime.today(), datetime.today())
db.session.add(open_internship1)

db_student2 = db.session.query(Student).filter(Student.registration_id == "STU2").one()
open_internship2 = OpenInternship("INT2", db_company1.id, "My title2", "My Description2", "7.15", "My comments2", datetime.today(), datetime.today())
db.session.add(open_internship2)
db.session.commit()

db_open_internship1 = db.session.query(OpenInternship).filter(OpenInternship.internship_code == "INT1").one()
db_open_internship2 = db.session.query(OpenInternship).filter(OpenInternship.internship_code == "INT2").one()
internship1 = Internship(db_open_internship1.id, db_university1.id, db_student1.id, "AVAILABLE")
internship2 = Internship(db_open_internship2.id, db_university1.id, db_student2.id, "AVAILABLE")

db.session.add(internship1)
db.session.add(internship2)

db.session.commit()
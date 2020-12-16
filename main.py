from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.address import Address
from model.base import Base
from model.company import Company
from model.internship import Internship
from model.program import Program
from model.student import Student
from model.university import University

engine = create_engine('mysql+pymysql://vub:vub1234!@127.0.0.1/vub', pool_recycle=3600)
metadata = MetaData(engine)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
address1 = Address("Distelstraat 6", "Schaerbeek", "Brussels", "Brussels", "Belgium", "1030")
address2 = Address("Hemeryckxlaan 10", "Kontich", "Antwerp", "Antwerp", "Belgium", "2660")
address3 = Address("Uitbreidingstraat 8", "Berchem", "Antwerp", "Antwerp", "Belgium", "2600")

company = Company("12345", "user@example.com", "UZA", "CPY1")
company.address = address1

program = Program("Masters in Applied Computer Science", "MACS")

student = Student("98765", "student@uni.be", "John", "Oliver", "Gates", "STU1")
student.address = address2
student.program = program

university = University("667788", "admin@uni.be", "UA", "UNI1")
university.address = address3
university.programs.append(program)

session.add(address1)
session.add(address2)
session.add(company)
session.add(program)
session.add(student)
session.add(university)
session.commit()

db_student = session.query(Student).filter(Student.id == 2).one()
db_university = session.query(University).filter(University.id == 3).one()
db_company = session.query(Company).filter(Company.id == 1).one()
internship = Internship("INT1", db_university.id, db_student.id, db_company.id, "AVAILABLE", datetime.today(),
                        datetime.today())

session.add(internship)
session.commit()

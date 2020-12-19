from flask import Flask, render_template

from model.address import Address
from model.student import Student
from model.user import User
from model.base import db
from model.address import Address
from model.company import Company
from model.internship import Internship
from model.program import Program
from model.student import Student
from model.university import University
from model.university_program import university_program
from model.base import app


@app.route("/")
def home():
    return "My flask app"


@app.route("/students")
def addresses():
    students = Student.query.all()
    return render_template("students.html", students=students)



if __name__ == "__main__":
    app.run(debug=True)
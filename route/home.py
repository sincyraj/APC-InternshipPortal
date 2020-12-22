from flask import Flask, render_template,url_for,request,session,logging,redirect,flash

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
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
def intership():
   return render_template("login.html")


@app.route("/login")
def login():
    return render_template("homepage.html")

@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    return render_template("students.html", students=students)


@app.route("/internships", methods=["GET"])
def get_internships():
    internships = Internship.query.all()
    return render_template("internships.html", internships=internships)


@app.route("/internship/change/status", methods=["POST"])
def post_internship_status():
    return "Done"


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, url_for, request, session, logging, redirect, flash

from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker
from wtforms import form

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
from service import internship_service, student_service


@app.route("/")
def page_not_found():
    return render_template("404.html")


@app.route("/login")
def login():
    return render_template("homepage.html")


@app.route("/students", methods=["GET"])
def get_students():
    students = student_service.fetch_all_students()
    return render_template("students.html", students=students)


@app.route("/internships", methods=["GET", "POST"])
def handle_internships():
    internships = internship_service.fetch_all_internships()

    if request.method == "POST":
        action = request.form.get("decision")
        internship_ids = request.form.getlist("updateStatus")
        internship_service.update_internships(action, internship_ids)
        return redirect(url_for("handle_internships"))
    return render_template("internships.html", internships=internships)



if __name__ == "__main__":
    app.run(debug=True)

from operator import and_

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
from model.open_internship import OpenInternship
from model.program import Program
from model.student import Student
from model.university import University
from model.university_program import university_program
from model.base import app
from service import internship_service, student_service


@app.route("/")
def page_not_found():
    return render_template("404.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        info = db.session.query(User).filter(User.user_name == username).one()
        if User.verify_hash(password, info.password_hash):
            print('user exist : ', info.user_name)
            print('category ', info.category)
        # If account exists in accounts table in out database
        if info:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = info.id
            session['username'] = info._user_name
            # Redirect to home page
            return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            return 'Incorrect username/password!'
    return render_template("homepage.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'category' in request.form and 'registration_id' in request.form and 'user_name' in request.form and 'password' in request.form and 'email' in request.form and 'phone_number' in request.form and 'first_name' in request.form and 'middle_name' in request.form and 'last_name' in request.form:
        # Create variables for easy access
        username = request.form['user_name']
        password = request.form['password']
        email = request.form['email']
        category = request.form['category']
        registration_id = request.form['registration_id']
        middle_name = request.form['middle_name']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        if category == 'student':
            student1 = Student(username, password, phone_number, email, first_name, middle_name, last_name,
                               registration_id)
            # address1 = Address("Distelstraat 6", "Schaerbeek", "Brussels", "Brussels", "Belgium", "1030")
            # program = Program("Masters in Applied Computer Science", "MACS")

            student1.address_id = 1
            student1.program_id = 1
            db.session.add(student1)
            db.session.commit()

    if request.method == 'POST' and 'category' in request.form and 'registration_id' in request.form and 'user_name' in request.form and 'password' in request.form and 'email' in request.form and 'phone_number' in request.form and 'first_name' in request.form:
        # Create variables for easy access
        print('unicheck!!!!!!')
        username = request.form['user_name']
        password = request.form['password']
        email = request.form['email']
        category = request.form['category']
        if category == 'company':
            company_code = request.form['registration_id']
        else:
            university_code = request.form['registration_id']
        name = request.form['first_name']
        phone_number = request.form['phone_number']
        if category == 'company':
            company = Company(username, password, phone_number, email, name, company_code)
            address1 = Address("Distelstraat 6", "Schaerbeek", "Brussels", "Brussels", "Belgium", "1030")
            company.address_id = 1
            db.session.add(company)
            db.session.commit()
            print('commitCHECK!!')

        elif (category == 'university'):
            university = University(username, password, phone_number, email, name, university_code)
            address3 = Address("Uitbreidingstraat 8", "Berchem", "Antwerp", "Antwerp", "Belgium", "2600")
            program = Program("Masters in Applied Computer Science", "MACS")

            university.address_id = 3
            # university.programs.append(program)
            db.session.add(university)
            db.session.commit()
            print('commitCHECK!!')
    return 'DONE!'


@app.route("/students", methods=['GET', 'POST'])
def get_students():
    student_id = 2  ##get from session
    internship_list = db.session.query(OpenInternship).filter(OpenInternship.student_id == student_id).all()
    print(internship_list)
    return render_template("students.html")


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
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)

from datetime import datetime
from operator import and_
from passlib.hash import pbkdf2_sha256

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
from model.open_internship import OpenInternship
from model.program import Program
from model.student import Student
from model.university import University
from model.university_program import university_program
from model.base import app
from service import internship_service, student_service
from flask_cors import CORS


@app.route("/")
def page_not_found():
    return render_template("404.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    a={}
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
            print ("in info check")
            session['loggedin'] = True
            session['id'] = info.id
            session['username'] = info.user_name
            # Redirect to home page
            return {'status':'0','category':info.category}
        else:
            # Account doesnt exist or username/password incorrect
            return {'status':'1','category':info.category}
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
    print("hello post")
    if request.method == 'POST':
        print ("hello post")
        student_id = 3 #get from session
        internship_id = request.form['internship_id']
        program_id = db.session.query(Student).filter(Student.id == student_id).one().program_id
        uni_programs = db.session.query(university_program).all()
        for val in uni_programs:
            if val.program_id == program_id:
                university_id = val.university_id
        print('UNI_ID : ',university_id)
        internship = Internship(internship_id,university_id,student_id,'APPLIED')
        db.session.add(internship)
        db.session.commit()

    student_id = 2  ##get from session
    internship_list = db.session.query(Internship).filter(Internship.student_id == student_id).all()
    #print(internship_list[0].internship_id)
    open_internships_list = db.session.query(OpenInternship).all()
    applied = []
    open_int = []
    for val in internship_list:
        tmp = []
        for op in open_internships_list:
            if op.id == val.id:
                tmp = [op.title,op.comments]
        applied.append([val.status] + tmp)
    print (applied)

    for val in open_internships_list:
        flag = False
        for app in internship_list:
            if app.id == val.id:
                flag = True
        if not flag:
            open_int.append({'id':val.id,'title':val.title,'description':val.description,'required_cgpa':val.required_cgpa,'start_date':val.start_date,'end_date':val.end_date})
    print (open_int)
    return {'data':open_int}

@app.route("/companies", methods=['GET', 'POST'])
def get_companies():
    company_id=1
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        gpa = request.form['required_gpa']
        internship_code=request.form['internship_code']
        comments=request.form['comments']
        print(title,description,gpa)
        open_internship2 = OpenInternship(internship_code, company_id, title, description,gpa
                                          ,comments, datetime.today(), datetime.today())
        db.session.add(open_internship2)
        db.session.commit()

    openInternship = db.session.query(OpenInternship).filter(OpenInternship.company_id == company_id).all()
    # open_internships_list = db.session.query(OpenInternship).all()
    values=[]
    for i in openInternship:
     internship_students = db.session.query(Internship).filter(and_(Internship.internship_id == i.id, Internship.status =="Approved")).all()

     for interns in internship_students:
         stu=db.session.query(Student).filter(Student.id==interns.student_id).one()
         values.append({'student':stu.first_name,'internship_code':i.internship_code,'required_cgpa':i.required_cgpa,'title' : i.title,'description' : i.description})
    return {'data':values}

@app.route("/internships", methods=["GET", "POST"])
def handle_internships():

    if request.method == "POST":
        action = request.form.get("decision")
        internship_ids = request.form.get("id")
        internship_service.update_internships(action, internship_ids)
        #return redirect(url_for("handle_internships"))
    internships = internship_service.fetch_all_internships()
    print(internships)
    values = []
    for intern in internships:
        internship_obj = db.session.query(OpenInternship).filter(OpenInternship.id == intern.internship_id).one()
        student_obj = db.session.query(Student).filter(Student.id==intern.student_id).one()
        values.append({'internship_id':intern.id,'first_name': student_obj.first_name,'last_name':student_obj.last_name,'student_cgpa':'3.5','title': internship_obj.title,'description':internship_obj.description,'required_gpa':internship_obj.required_cgpa})
    return {'data':values}


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    CORS(app)

    app.run(debug=True)

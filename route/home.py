from flask import Flask, render_template

from model.student import Student
from model.user import User

app = Flask(__name__)


@app.route("/")
def home():
    return "My flask app"


@app.route("/students")
def users():
    students = Student.query.all()
    return render_template("students.html", students=students)



if __name__ == "__main__":
    app.run(debug=True)
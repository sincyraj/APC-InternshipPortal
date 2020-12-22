from model.student import Student

def fetch_all_students():
    return Student.query.all()
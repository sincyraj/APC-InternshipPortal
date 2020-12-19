from base import db

class Program(db.Model):
    __tablename__ = "program"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    program_code = db.Column(db.String(50), unique=True)

    def __init__(self, name, program_code):
        self.name = name
        self.program_code = program_code

    def __repr__(self):
        return "Program Name %s" % self.name


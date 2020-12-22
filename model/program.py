from model.base import db

class Program(db.Model):
    __tablename__ = "program"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    program_code = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name, program_code):
        self.name = name
        self.program_code = program_code

    def __repr__(self):
        return "Program Name %s" % self.name


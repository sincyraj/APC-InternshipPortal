from model.base import db

university_program = db.Table('university_program', db.metadata,
    db.Column('university_id', db.Integer, db.ForeignKey('university.id')),
    db.Column('program_id', db.Integer, db.ForeignKey('program.id'))
)
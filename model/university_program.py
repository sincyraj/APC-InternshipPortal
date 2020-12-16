from sqlalchemy import Column, ForeignKey, Integer, Table

from model.base import Base

university_program = Table('university_program', Base.metadata,
    Column('university_id', Integer, ForeignKey('university.id')),
    Column('program_id', Integer, ForeignKey('program.id'))
)
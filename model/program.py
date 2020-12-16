
from sqlalchemy import Column, Integer, String

from model.base import Base


class Program(Base):
    __tablename__ = "program"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    program_code = Column(String(50), unique=True)

    def __init__(self, name, program_code):
        self.name = name
        self.program_code = program_code

    def __repr__(self):
        return "Program Name %s" % self.name


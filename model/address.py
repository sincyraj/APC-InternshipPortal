
from sqlalchemy import Column, Integer, String

from model.base import Base


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    address_line1 = Column(String(100))
    address_line2 = Column(String(100))
    city = Column(String(50))
    province = Column(String(50))
    country = Column(String(50))
    zip_code = Column(String(50))

    def __init__(self, address_line1, address_line2, city, province, country, zip_code):
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.province = province
        self.country = country
        self.zip_code = zip_code

    def __repr__(self):
        return "Address %s" % self.name

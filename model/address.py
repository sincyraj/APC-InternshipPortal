from base import db
class Address(db.Model):
    __tablename__ = "address"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address_line1 = db.Column(db.String(100))
    address_line2 = db.Column(db.String(100))
    city = db.Column(db.String(50))
    province = db.Column(db.String(50))
    country = db.Column(db.String(50))
    zip_code = db.Column(db.String(50))

    def __init__(self, address_line1, address_line2, city, province, country, zip_code):
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.province = province
        self.country = country
        self.zip_code = zip_code

    def __repr__(self):
        return "Address %s" % self.name

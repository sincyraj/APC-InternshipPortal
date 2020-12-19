from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="../templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://vub:vub1234!@127.0.0.1/vub'
db = SQLAlchemy(app)
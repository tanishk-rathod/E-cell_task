from __main__ import db

class Startup(db.Model):
    S_no = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), primary_key=False, nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Phone_num = db.Column(db.Integer, primary_key=False, nullable=False)
    Startupname = db.Column(db.String(80), primary_key=False, nullable=False)
    Teamnumber = db.Column(db.String(80), primary_key=False, nullable=False)
class Attendies(db.Model):
    S_no = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), primary_key=False, nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Phone_num = db.Column(db.Integer, primary_key=False, nullable=False)
    City = db.Column(db.String(80), primary_key=False, nullable=False)
    College = db.Column(db.String(80), primary_key=False, nullable=True)
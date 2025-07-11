from app import db 

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contestant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)  # 👈 MUST be here if you use age
    occupation = db.Column(db.String(200))  # 👈 add if you're using this too
    bio = db.Column(db.Text)
    status = db.Column(db.String(50))  # Optional
    photo_url = db.Column(db.String(250))  # Optional


class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    air_date = db.Column(db.Date)
    summary = db.Column(db.Text)

    
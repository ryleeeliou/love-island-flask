from app import db 

class Contestant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.String(200))
    bio = db.Column(db.Text)
    status = db.Column(db.String(20)) #coupled vs single

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    air_date = db.Column(db.Date)
    summary = db.Column(db.Text)

    
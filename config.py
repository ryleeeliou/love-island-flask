import os 
#basedir makes sure SQLite file lives alongside script
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    #DATABASE_URL from environment or fallback to sqlite
    #Tell SQLAlchemy where to find or create database
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or f"sqlite:///{os.path.join(basedir, 'app.db')}"

    )

    #no signal tracking to save resources 
    SQLALCHEMY_TRACK_MODIFICATIONS = False 


    #secret key secures forms
    SECRET_KEY = os.environ.get("SECRET_KEY", "you-should-change-this")
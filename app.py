from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from config import Config 

#instantiate flask app and settings

app = Flask(__name__)
app.config.from_object(Config)

#set database and migration engine 

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#import models so they can be detected by flask

from models import Contestant, Episode 


#routes and views here later

if __name__ == "__main__":
    app.run(debug=True)
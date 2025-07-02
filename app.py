from flask import Flask, render_template, url_for
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

@app.route("/")
def index():
    contestants = Contestant.query.all()
    return render_template("index.html", contestants=contestants)

@app.route("/contestant/<int:id>")
def show_contestant(id):
    c = Contestant.query.get_or_404(id)
    return render_template("contestant.html", c=c)


#routes and views here later

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, url_for
from config import Config 
from models import db, Contestant


#instantiate flask app and settings

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

#import models so they can be detected by flask


@app.route("/")
def index():
    contestants = Contestant.query.all()
    return render_template("index.html", contestants=contestants)

@app.route("/contestant/<int:id>")
def show_contestant(id):
    contestant = Contestant.query.get_or_404(id)
    return f"<h1>{contestant.name}</h1><p>Partner: {contestant.partner or 'Single'}</p>"


#routes and views here later

if __name__ == "__main__":
    app.run(debug=True)
from app import app, db
from models import Contestant 

with app.app_context():
    db.create_all()

    contestants = [
        Contestant(name="Ace", age=22, occupation="Dance Teacher (Teaches people on TikTok...)"),
        Contestant(name="Chelley", age=27, occupation="Day Trade (Stock market boss lady!)"),
        Contestant(name="Amaya", age=25, occupation="Nurse (Cardio ICU...she means business)"),
        Contestant(name="Bryan", age=28, occupation="Accountant, Realtor, Bartender--jack of all trades!"),
        Contestant(name="Chris", age=27, occupation="Basketball Player (Overseas to be specific)"),
        Contestant(name="Huda", age=24, occupation="Fitness coach and mamacita <3"),    
        Contestant(name="Iris", age=25, occupation="Social Media Influncer (consider me influenced)"),
        Contestant(name="Pepe", age=27, occupation="Retired Basketball Player (also overseas...I sense a theme)"),
        Contestant(name="Nic", age=24, occupation="Nurse? We think?"),
        Contestant(name="Olandria", age=27, occupation="Sales Specialist (she sells elevators...I'm sold!")]

    db.session.add_all(contestants)
    db.session.commit()
    print("Database seeded successfully!")
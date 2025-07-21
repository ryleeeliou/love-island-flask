from app import app, db
from models import Contestant 

with app.app_context():
    # Reset the database
    db.drop_all()
    db.create_all()

    # ✅ Define contestants
    ace = Contestant(name="Ace", age=22, occupation="Dance Teacher (Teaches people on TikTok...)")
    chelley = Contestant(name="Chelley", age=27, occupation="Day Trade (Stock market boss lady!)")
    amaya = Contestant(name="Amaya", age=25, occupation="Nurse (Cardio ICU...she means business)")
    bryan = Contestant(name="Bryan", age=28, occupation="Accountant, Realtor, Bartender--jack of all trades!")
    chris = Contestant(name="Chris", age=27, occupation="Basketball Player (Overseas to be specific)")
    huda = Contestant(name="Huda", age=24, occupation="Fitness coach and mamacita <3")
    iris = Contestant(name="Iris", age=25, occupation="Social Media Influencer (consider me influenced)")
    pepe = Contestant(name="Pepe", age=27, occupation="Retired Basketball Player (also overseas...I sense a theme)")
    nic = Contestant(name="Nic", age=24, occupation="Nurse? We think?")
    olandria = Contestant(name="Olandria", age=27, occupation="Sales Specialist (she sells elevators...I'm sold!)")

    # ✅ Set partner relationships
    ace.partner = "Chelley"
    chelley.partner = "Ace"
    amaya.partner = "Bryan"
    bryan.partner = "Amaya"
    chris.partner = "Huda"
    huda.partner = "Chris"
    iris.partner = "Pepe"
    pepe.partner = "Iris"
    nic.partner = "Olandria"
    olandria.partner = "Nic"

    # ✅ Add all to the session
    db.session.add_all([ace, chelley, amaya, bryan, chris, huda, iris, pepe, nic, olandria])
    db.session.commit()
    print("Database seeded successfully!")

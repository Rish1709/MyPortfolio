from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PersonalInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    school = db.Column(db.String(200))
    class_x_grade = db.Column(db.String(20))
    class_xii_grade = db.Column(db.String(20))
    jeemains_rank = db.Column(db.String(20))
    jeeadv_rank = db.Column(db.String(20))
    college = db.Column(db.String(200))
    achievements = db.Column(db.Text)
    hobbies = db.Column(db.Text)
    interests = db.Column(db.Text)
    projects = db.Column(db.Text)
    resume = db.Column(db.Text)

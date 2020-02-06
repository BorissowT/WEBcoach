from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Teacher(db.Model):
    __tablename__ = "teacher"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True, nullable=False)
    about = db.Column(db.String(500),unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    goals = db.relationship("Goals", uselist=False, back_populates="teacher")
    free = db.Column(db.JSON, nullable=False)
    booking = db.relationship("Booking", back_populates="teacher")


class Goals(db.Model):
    __tablename__ = 'goals'
    id = db.Column(db.Integer, primary_key=True)
    travel = db.Column(db.Boolean, nullable=False)
    study = db.Column(db.Boolean, nullable=False)
    work = db.Column(db.Boolean, nullable=False)
    relocate = db.Column(db.Boolean, nullable=False)

    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    teacher = db.relationship("Teacher", back_populates="goals")


class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(50), nullable=False)
    day = db.Column(db.String(51), nullable=False)
    time = db.Column(db.Integer, nullable=False)

    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    teacher = db.relationship("Teacher", back_populates="booking")


class Request(db.Model):
    __tablename__ = 'request'
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(10), nullable=False)
    time = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(50), nullable=False)
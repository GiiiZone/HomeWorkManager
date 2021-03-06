from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class ElectiveCourse(db.Model):
    __tablename__ = 'elective_course'

    user_id = db.Column(db.String, db.ForeignKey("user.id"), primary_key=True)
    course_id = db.Column(db.String, db.ForeignKey("course.id"), primary_key=True)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(54), primary_key=True)
    username = db.Column(db.String(54), unique=True)
    passwdhash = db.Column(db.String(54))
    identity = db.Column(db.String(4))

    is_authenticated = True
    is_active = True
    is_anonymous = False

    def __init__(self, id,username, password,identity):
        self.id = id
        self.username = username
        self.set_password(password)
        self.identity = identity

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.passwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwdhash, password)

    def get_username(self):
        return self.username

    def get_indentity(self):
        return self.identity


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.String(54), primary_key=True)
    course_name = db.Column(db.String(54))

    homework = db.relationship("HomeWork", lazy='dynamic')
    users = db.relationship("User", secondary='elective_course', backref="courses", lazy='dynamic')

    def __init__(self, id,course_name):
        self.id = id
        self.course_name = course_name


class HomeWork(db.Model):
    __tablename__ = 'homework'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(54), db.ForeignKey('course.id'))
    batch = db.Column(db.Integer)
    homework_name = db.Column(db.String(120))
    publish_time = db.Column(db.String(24))
    end_time = db.Column(db.String(24))
    upload_status = db.Column(db.String(24))
    status = db.Column(db.String(24))

    def __init__(self, course_name,batch, homework_name,publish_time,end_time,upload_status,status):
        self.course_name = course_name
        self.batch = batch
        self.homework_name = homework_name
        self.publish_time = publish_time
        self.end_time = end_time
        self.upload_status = upload_status
        self.status = status


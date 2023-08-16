from .db import  db

class User(db.Document):
    fullName=db.StringField(required=True)
    email=db.StringField(required=True)
    password=db.StringField(required=True)
    phone=db.StringField(required=True)
    cnic=db.StringField(required=True)

import sqlite3
from db import db 
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    password = Column(String(80))

    def __init__(self, _id, username, password):  ## _id because id is keyword in python
        self.id = _id
        self.username = username
        self.password = password
    

## those api acts as an interface to our db objects

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def findByUsername(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def findByUserId(cls, _id):
        return cls.query.filter_by(id=_id).first()
         

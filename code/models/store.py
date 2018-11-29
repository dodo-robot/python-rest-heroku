import sqlite3
from db import db 
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))

    items = db.relationship('ItemModel', lazy="dynamic")

    def __init__(self, name):  ## _id because id is keyword in python
        self.name = name 

    def json(self):
        return { 'name': self.name, 'items': [ item.json() for item in self.items.all() ] }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.add(self)
        db.session.commit() 
        

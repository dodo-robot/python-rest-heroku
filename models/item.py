import sqlite3
from db import db 
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    price = Column(Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, _id, name, price, store_id):  ## _id because id is keyword in python
        self.id = _id
        self.name = name
        self.price = price 
        self.store_id = store_id

    def json(self):
        return { 'id': self.id, 'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.add(self)
        db.session.commit() 
        

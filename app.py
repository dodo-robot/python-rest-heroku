from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserController
from resources.item import ItemListController, ItemController
from resources.store import StoreListController, StoreController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 's3cr3t'
api = Api(app) ## esay usage of GET POST DELETE

jwt = JWT(app, authenticate, identity) ## /auth

api.add_resource(StoreController, '/store/<string:name>')
api.add_resource(ItemController, '/item/<string:name>')
api.add_resource(ItemListController, '/items')
api.add_resource(UserController, '/register')
api.add_resource(StoreListController, '/stores')

## this method will not run in heroku su we create run.py
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
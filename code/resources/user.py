import sqlite3
from models.user import UserModel
from flask_restful import Resource, reqparse

class UserController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type=str,
        required=True,
        help='This field is required'
    )
    parser.add_argument('password', 
        type=str,
        required=True,
        help='This field is required'
    )

    def post(self):      
        data = UserController.parser.parse_args()

        if(UserModel.findByUsername(data['username'])):
            return {"message" : "User with that username already exists!"}, 400

        user = UserModel(None, data['username'],data['password'])
        user.save_to_db()
        
        return {"message" : "User created!"}, 201



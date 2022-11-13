from flask import request
from flask_restful import Resource



class Testing(Resource):

    def get(self):
        a = request.args.get('name')
        userId = request.args.get('userId')
        if a is not None:
            return {'data': {'userID': userId, 'name': a}}, 200
        else:
            return {"msg": "need input for \"name\""}, 400
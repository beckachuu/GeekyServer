import google.auth.transport.requests
import requests
from flask import redirect, request, session
from flask_restful import Resource

from src.const import MESSAGE
from src.controller.auth import login_required


class Search(Resource):
    def get(self):
        book_results = ["book1", "book2"]
        author_results = ["author1", "author2"]
        userId = request.args.get('userId')
        return {MESSAGE: "search successful"}, 200


class Recommendation(Resource):
    def get(self):
        book_list = []
        return book_list

    @login_required()
    def post(self):
        # Send user's activity to update recommendatión
        return {MESSAGE: "suceeded"}

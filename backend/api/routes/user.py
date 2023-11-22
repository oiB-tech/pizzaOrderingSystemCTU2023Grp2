from flask import request
from flask_restplus import Resource
from .. import api_main as api

@api.route('/users')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {}

    def put(self, todo_id):
        return {}
from flask_restplus import fields, Resource
from ..api import api_main as api

user_model = api.model('User', {
    "userId": fields.String,
    "username": fields.String,
    "hash": fields.String,
    "salt": fields.String,
    "firstName": fields.String,
    "lastName": fields.String,
    "phoneNumber": fields.String,
    "activeCart": fields.String,
})
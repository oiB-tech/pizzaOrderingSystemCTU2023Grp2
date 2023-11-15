from flask_restplus import fields, Resource
from ..api import api_main as api

user_model = api.model('Address', {
    "addressId": fields.String,
    "addressLine1": fields.String,
    "addressLine2": fields.String,
    "city": fields.String,
    "stateCode": fields.String,
    "zipCode": fields.String,
})
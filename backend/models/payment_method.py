from flask_restplus import fields, Resource
from ..api import api_main as api

user_model = api.model('PaymentMethod', {
    "cardNumber": fields.String,
    "cardExpDate": fields.String,
    "cardCvv": fields.String,
    "cardCardholderName": fields.String,
    "cardId": fields.String,
    "billingAddress": fields.String,
})
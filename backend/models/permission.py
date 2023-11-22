from flask_restplus import fields, Resource
from ..api import api_main as api

permission_model = api.model('Permissions', {
    "permissionName": fields.String,
})
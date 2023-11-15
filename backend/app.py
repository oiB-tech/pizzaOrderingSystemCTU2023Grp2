from flask import Flask
from .api import api_main as api

app = Flask(__name__)

@api.route("/")
class FrontendServer():
    def get(self):
        return "<p>Hello, World!</p>"
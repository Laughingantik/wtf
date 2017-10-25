from flask import Flask
import api


app = Flask(__name__)
api.register(app)

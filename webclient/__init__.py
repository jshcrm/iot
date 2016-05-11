from flask import Flask
from flask.ext.pymongo import PyMongo

webclient = Flask(__name__)
mongo = PyMongo(webclient)
from webclient import views

from flask import Flask

webclient = Flask(__name__)
from webclient import views

# Imports
from flask import Blueprint

# SetUp
api = Blueprint('api', __name__)

# Routes
@api.route('/')
def index():
    return 'urls index route'

from flask import Blueprint

bp = Blueprint('formsubmit', __name__)

from app.formsubmit import routes

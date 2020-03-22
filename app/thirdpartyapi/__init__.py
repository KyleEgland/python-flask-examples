from flask import Blueprint

bp = Blueprint('thirdpartyapi', __name__)

from app.thirdpartyapi import routes

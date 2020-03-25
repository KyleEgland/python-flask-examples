from flask import render_template
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    # Render index page
    return render_template('index.html')


@bp.route('/about')
def about():
    # Render about page
    return render_template('about.html')

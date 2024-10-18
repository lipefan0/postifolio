from flask import Blueprint, render_template
from app.data import data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', skills=data['skills'], projects=data['projects'])

@main.route('/projects')
def projects():
    return render_template('projects.html', projects=data['projects'])

@main.route('/contact')
def contact():
    return render_template('contact.html')
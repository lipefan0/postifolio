from flask import Flask
from app.views.main_views import main
import os

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
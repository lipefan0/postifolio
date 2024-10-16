from flask import Flask, render_template
import os
from app.data import skills, projects as project_list 

app = Flask(__name__, template_folder=os.path.join('app', 'templates'), static_folder=os.path.join('app', 'static'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', skills=skills, projects=project_list)

@app.route('/projects', methods=['GET'])
def show_projects():  # Renomeie a função aqui
    return render_template('projects.html', projects=project_list)

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/contato', methods=['GET'])
def contato():
    return render_template('contato.html')



if __name__ == '__main__':
    app.run(debug=True, port=5001)

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# If you don't need a database yet, comment out the next 3 lines:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/tasks', methods=['GET'])

@app.route('/')

def home():
    return "Welcome to Resumind! Try /tasks to see tasks."

def get_tasks():
    return {"tasks": ["Buy milk", "Update resume"]}

# run the Flask app and create a database 
if __name__ == '__main__':
    app.run(debug=True)
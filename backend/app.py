from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # avoids a warning

# initialize SQLAlchemy instance
db = SQLAlchemy(app)

# run the Flask app and create a database 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
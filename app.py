from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, request, render_template

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:hacker1@localhost:5432/users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"<User {self.name}>"
    @app.route('/', methods=['GET'])
    def users1():
        return  render_template('index.html')
if __name__ == "__main__":
    app.run()

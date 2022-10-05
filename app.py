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
    email=db.Column(db.String())
    age=db.Column(db.String())
    gender=db.Column(db.String())
    mobile=db.Column(db.String())
    address=db.Column(db.String())

    def __init__(self, name, password,email,age,gender,mobile,address):
        self.name = name
        self.password = password
        self.email=email
        self.age=age
        self.gender=gender
        self.mobile=mobile
        self.address=address
    
    def __repr__(self):
        return f"<User {self.name}>"
    @app.route('/', methods=['GET'])
    def users1():
        return  render_template('index.html')
    @app.route('/logn', methods=['GET'])
    def users2():
        return  render_template('logn.html')
    @app.route('/sgnup', methods=['GET'])
    def users3():
        return  render_template('sgnup.html')
    @app.route('/home', methods=['GET'])
    def users4():
        return  render_template('home.html')
    @app.route('/product', methods=['GET'])
    def users5():
        return  render_template('product.html')
    @app.route('/cart',methods=['GET'])
    def users6():
        return render_template('cart.html')
    @app.route('/users', methods=['POST', 'GET'])
    def handle_users():
        if request.method == 'POST':
            if request.form:
                data = request.form
                new_user = UsersModel(name=data['name'], password=data['phone'],email=data['email'],age=data['date'],gender=data['time'],mobile=data['people'],address=data['message'])
                db.session.add(new_user)
                db.session.commit()
                return {"message": f"user {new_user.name} has been created successfully."}
            else:
                return {"error": "No data passed in form."}

        elif request.method == 'GET':
            users = UsersModel.query.all()
            results = [
                {
                    "name": user.name
                } for user in users]

            return {"count": len(results), "users": results}
    
if __name__ == "__main__":
    app.run()

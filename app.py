import json

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import data
# from models import Users, Orders, Offers
import utils

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Orders(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    start_date = db.Column(db.Integer)
    end_date = db.Column(db.String(100))
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id,
        }


class Offers(db.Model):
    __tablename__ = "offer"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }


def init_database():
    db.drop_all()
    db.create_all()

    for user in data.users:
        db.session.add(
            Users(
                id=user.get("id"),
                first_name=user.get("first_name"),
                last_name=user.get("last_name"),
                age=user.get("age"),
                email=user.get("email"),
                role=user.get("role"),
                phone=user.get("phone"),
            )
        )
        db.session.commit()

    for order in data.orders:
        db.session.add(
            Orders(
                id=order.get("id"),
                name=order.get("name"),
                description=order.get("description"),
                start_date=order.get("start_date"),
                end_date=order.get("end_date"),
                address=order.get("address"),
                price=order.get("price"),
                customer_id=order.get("customer_id"),
                executor_id=order.get("executor_id"),
            )
        )
        db.session.commit()

    for offer in data.offers:
        db.session.add(
            Offers(
                id=offer.get("id"),
                order_id=offer.get("order_id"),
                executor_id=offer.get("executor_id"),
            )
        )
        db.session.commit()


init_database()


@app.route("/users")
def get_all_users():
    res = []
    users = Users.query.all()
    for user in users:
        res.append(user.to_dict())
    return jsonify(res)


@app.route("/users/<int:pk>")
def users_by_pk(pk):
    user = Users.query.get(pk)
    return jsonify(user.to_dict())


@app.route("/orders")
def get_all_orders():
    res = []
    orders = Orders.query.all()
    for order in orders:
        res.append(order.to_dict())
    return jsonify(res)


@app.route("/orders/<int:pk>")
def orders_by_pk(pk):
    order = Orders.query.get(pk)
    return jsonify(order.to_dict())


@app.route("/offers")
def get_all_offers():
    res = []
    offers = Offers.query.all()
    for offer in offers:
        res.append(offer.to_dict())
    return jsonify(res)


@app.route("/offers/<int:pk>")
def offers_by_pk(pk):
    order = Offers.query.get(pk)
    return jsonify(order.to_dict())


if __name__ == '__main__':
    app.run(debug=True, port=5001)

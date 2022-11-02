import json
from flask import Blueprint, jsonify, request
from app import db
from app.models import Orders

# create blueprint
order_blueprint = Blueprint("order_blueprint", __name__)


@order_blueprint.route("/orders", methods=["GET", "POST"])
def get_all_orders():
    if request.method == "GET":
        res = []
        orders = Orders.query.all()
        for order in orders:
            res.append(order.to_dict())
        return jsonify(res)

    if request.method == "POST":
        # get data from request
        order_data = json.loads(request.data)
        # create new order
        user = Orders(
            id=order_data.get("id"),
            name=order_data.get("name"),
            description=order_data.get("description"),
            start_date=order_data.get("start_date"),
            end_date=order_data.get("end_date"),
            address=order_data.get("address"),
            price=order_data.get("price"),
            customer_id=order_data.get("customer_id"),
            executor_id=order_data.get("executor_id"),
        )
        db.session.add(user)
        db.session.commit()
        return "Order successfully added!"


@order_blueprint.route("/orders/<int:pk>", methods=["GET", "PUT", "DELETE"])
def order_by_pk(pk):
    if request.method == "GET":
        order = Orders.query.get(pk)
        return jsonify(order.to_dict())
    if request.method == "PUT":
        # get data from request
        order_data = json.loads(request.data)
        # get data from database and change

        order = Orders.query.get(pk)
        order.name = order_data.get("name")
        order.description = order_data.get("description")
        order.start_date = order_data.get("start_date")
        order.end_date = order_data.get("end_date")
        order.address = order_data.get("address")
        order.price = order_data.get("price")
        order.customer_id = order_data.get("customer_id")
        order.executor_id = order_data.get("executor_id")

        db.session.add(order)
        db.session.commit()
        return "User successfully updated!"

    if request.method == "DELETE":
        order = Orders.query.get(pk)
        db.session.delete(order)
        db.session.commit()
        return "User successfully deleted!"

from flask import Blueprint, jsonify
from app.models import Orders

order_blueprint = Blueprint("order_blueprint", __name__)

@order_blueprint.route("/orders")
def get_all_orders():
    res = []
    orders = Orders.query.all()
    for order in orders:
        res.append(order.to_dict())
    return jsonify(res)


@order_blueprint.route("/orders/<int:pk>")
def order_by_pk(pk):
    order = Orders.query.get(pk)
    return jsonify(order.to_dict())
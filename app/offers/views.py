import json
from flask import Blueprint, jsonify, request
from app import db
from app.models import Offers

# create blueprint
offer_blueprint = Blueprint("offer_blueprint", __name__)


@offer_blueprint.route("/offers", methods=["GET", "POST"])
def get_all_offers():
    if request.method == "GET":
        res = []
        offers = Offers.query.all()
        for offer in offers:
            res.append(offer.to_dict())
        return jsonify(res)

    if request.method == "POST":
        # get data from request
        offer_data = json.loads(request.data)
        # create new offer
        offer = Offers(
            id=offer_data.get("id"),
            order_id=offer_data.get("order_id"),
            executor_id=offer_data.get("executor_id"),
        )
        db.session.add(offer)
        db.session.commit()
        return "Offer successfully added!"


@offer_blueprint.route("/offers/<int:pk>", methods=["GET", "PUT", "DELETE"])
def offer_by_pk(pk):
    if request.method == "GET":
        offer = Offers.query.get(pk)
        return jsonify(offer.to_dict())
    if request.method == "PUT":
        # get data from request
        offer_data = json.loads(request.data)
        # get data from database and change
        offer = Offers.query.get(pk)
        offer.id = offer_data.get("id")
        offer.order_id = offer_data.get("order_id")
        offer.executor_id = offer_data.get("executor_id")

        db.session.add(offer)
        db.session.commit()
        return "Offer successfully updated!"

    if request.method == "DELETE":
        offer = Offers.query.get(pk)
        db.session.delete(offer)
        db.session.commit()
        return "Offer successfully deleted!"

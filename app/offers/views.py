from flask import Blueprint, jsonify
from app.models import Offers

offer_blueprint = Blueprint("offer_blueprint", __name__)


@offer_blueprint.route("/offers")
def get_all_offers():
    res = []
    offers = Offers.query.all()
    for offer in offers:
        res.append(offer.to_dict())
    return jsonify(res)


@offer_blueprint.route("/offers/<int:pk>")
def offer_by_pk(pk):
    offer = Offers.query.get(pk)
    return jsonify(offer.to_dict())

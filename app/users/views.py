from flask import Blueprint, jsonify
from app.models import Users

user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("/users")
def get_all_users():
    res = []
    users = Users.query.all()
    for user in users:
        res.append(user.to_dict())
    return jsonify(res)


@user_blueprint.route("/users/<int:pk>")
def users_by_pk(pk):
    user = Users.query.get(pk)
    return jsonify(user.to_dict())
import json
from flask import Blueprint, jsonify, request
from app import db
from app.models import Users

# create blueprint
user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route("/users", methods=["GET", "POST"])
def get_all_users():
    if request.method == "GET":
        res = []
        users = Users.query.all()
        for user in users:
            res.append(user.to_dict())
        return jsonify(res)

    if request.method == "POST":
        # get data from request
        user_data = json.loads(request.data)
        # create new user
        user = Users(
            id=user_data.get("id"),
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            age=user_data.get("age"),
            email=user_data.get("email"),
            role=user_data.get("role"),
            phone=user_data.get("phone"),
        )
        db.session.add(user)
        db.session.commit()
        return "User successfully added!"


@user_blueprint.route("/users/<int:pk>", methods=["GET", "PUT", "DELETE"])
def users_by_pk(pk):
    if request.method == "GET":
        user = Users.query.get(pk)
        return jsonify(user.to_dict())

    if request.method == "PUT":
        # get data from request
        user_data = json.loads(request.data)
        # get data from database and change
        user = Users.query.get(pk)
        user.first_name = user_data.get("first_name")
        user.last_name = user_data.get("last_name")
        user.age = user_data.get("age")
        user.email = user_data.get("email")
        user.role = user_data.get("role")
        user.phone = user_data.get("phone")

        db.session.add(user)
        db.session.commit()
        return "User successfully updated!"

    if request.method == "DELETE":
        user = Users.query.get(pk)
        db.session.delete(user)
        db.session.commit()
        return "User successfully deleted!"

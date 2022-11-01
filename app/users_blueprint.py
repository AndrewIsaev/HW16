from flask import Blueprint

user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("/users")
def all_users():
    result = []
    users = User.qe
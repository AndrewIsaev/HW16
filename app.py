from app import app
from app.users_blueprint import user_blueprint
from utils import init_database

app.register_blueprint(user_blueprint)
init_database()


if __name__ == '__main__':
    app.run(port=5003)
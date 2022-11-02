from app import app
from app.offers.views import offer_blueprint
from app.orders.views import order_blueprint
from app.users.views import user_blueprint
from utils import init_database

app.register_blueprint(user_blueprint)
app.register_blueprint(offer_blueprint)
app.register_blueprint(order_blueprint)
init_database()


if __name__ == '__main__':
    app.run()
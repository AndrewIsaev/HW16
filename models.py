from app import db


class Users(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def users_to_dict(self, raw_data):
        for item in raw_data:
            result = []
            result.append(
                Users(
                    id=item.get("id"),
                    first_name=item.get("first_name"),
                    last_name=item.get("last_name"),
                    age=item.get("age"),
                    email=item.get("email"),
                    role=item.get("role"),
                    phone=item.get("phone"),
                )
            )
            return result


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
    executor = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("Users")

    def orders_to_dict(self, raw_data):
        for item in raw_data:
            result = []
            result.append(
                Users(
                    id=item.get("id"),
                    name=item.get("name"),
                    description=item.get("description"),
                    start_date=item.get("start_date"),
                    end_date=item.get("end_date"),
                    address=item.get("address"),
                    price=item.get("price"),
                    customer_id=item.get("customer_id"),
                    executor_id=item.get("executor_id"),
                )
            )
            return result


class Offers(db.Model):
    __tablename__ = "offer"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    order = db.relationship("Orders")
    user = db.relationship("Users")

    def offers_to_dict(self, raw_data):
        for item in raw_data:
            result = []
            result.append(
                Users(
                    id=item.get("id"),
                    order_id=item.get("order_id"),
                    executor_id=item.get("executor_id"),
                )
            )
            return result

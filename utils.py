import data
from app import db
import app.models as models


def init_database() -> None:
    """
    Init database from json data
    :return: None
    """
    db.drop_all()
    db.create_all()

    # fill user table
    for user in data.users:
        db.session.add(
            models.Users(
                id=user.get("id"),
                first_name=user.get("first_name"),
                last_name=user.get("last_name"),
                age=user.get("age"),
                email=user.get("email"),
                role=user.get("role"),
                phone=user.get("phone"),
            )
        )
        db.session.commit()

    # fill order table
    for order in data.orders:
        db.session.add(
            models.Orders(
                id=order.get("id"),
                name=order.get("name"),
                description=order.get("description"),
                start_date=order.get("start_date"),
                end_date=order.get("end_date"),
                address=order.get("address"),
                price=order.get("price"),
                customer_id=order.get("customer_id"),
                executor_id=order.get("executor_id"),
            )
        )
        db.session.commit()

    # fill offer table
    for offer in data.offers:
        db.session.add(
            models.Offers(
                id=offer.get("id"),
                order_id=offer.get("order_id"),
                executor_id=offer.get("executor_id"),
            )
        )
        db.session.commit()

# def init_database():
#     import app
#     import models
#     import data
#     app.db.drop_all()
#     app.db.create_all()
#
#     for user in data.users:
#         app.db.session.add(
#             models.Users(
#                 id=user.get("id"),
#                 first_name=user.get("first_name"),
#                 last_name=user.get("last_name"),
#                 age=user.get("age"),
#                 email=user.get("email"),
#                 role=user.get("role"),
#                 phone=user.get("phone"),
#             )
#         )
#         app.db.session.commit()
#
#     for order in data.orders:
#         app.db.session.add(
#             models.Orders(
#                 id=order.get("id"),
#                 name=order.get("name"),
#                 description=order.get("description"),
#                 start_date=order.get("start_date"),
#                 end_date=order.get("end_date"),
#                 address=order.get("address"),
#                 price=order.get("price"),
#                 customer_id=order.get("customer_id"),
#                 executor_id=order.get("executor_id"),
#             )
#         )
#         app.db.session.commit()
#
#     for offer in data.offers:
#         app.db.session.add(
#             models.Offers(
#                 id=offer.get("id"),
#                 order_id=offer.get("order_id"),
#                 executor_id=offer.get("executor_id"),
#             )
#         )
#         app.db.session.commit()

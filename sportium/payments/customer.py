from users.models import User

from . import stripe


def create_customer(user):
    customer = stripe.Customer.create(
        description=user.description  # Una simple descripción del usuario
    )
    return customer


user = User.objects.get(pk=1)

customer = create_customer(user)

user.customer_id = customer.id
user.save()

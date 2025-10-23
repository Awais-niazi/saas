import stripe
from decouple import config

DJANGO_DEBUG = config("DJANGO_DEBUG", default=False, cast=bool)
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", default=None, cast=str) 

if "sk_test" in STRIPE_SECRET_KEY and not DJANGO_DEBUG:
    raise ValueError("Using test Stripe secret key in production is not allowed.")

stripe.api_key = STRIPE_SECRET_KEY

def create_costomer():
    customer = stripe.Customer.create(
    name="Jenny Rosen",
    email="jennyrosen@example.com",
)
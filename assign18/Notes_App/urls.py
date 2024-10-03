from main import app
from methods import *


# register routes 
app.add_url_rule(endpoint="/register", view_func=register, methods=["POST"],rule="/register")


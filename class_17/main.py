from flask import Flask

app:Flask = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/users")
def users():
    return "Hello User"

# path params
@app.route("/users?status=1&limit=10", methods=["GET"])
def get_users():
    return "Get Users"

# raw params
@app.route("/users", methods=["POST"])




@app.route("/users", methods=["POST"])
def create_user():
    return "User created"

@app.route("/users/<int:id>")
def user(id):
    return f"Hello User {id}"

@app.route("/users/<int:id>/posts")
def user_posts(id):
    return f"Posts from User {id}"

@app.route("/users/<int:id>/posts/<int:post_id>")
def user_post(id, post_id):
    return f"Post {post_id} from User {id}"


app.run(
    debug=True, 
    host="localhost",
    port=3000
)






import db
from flask import Flask, jsonify, request

db_conn = db.mysqlconnect()
app:Flask = Flask(__name__)

#  get all books
@app.route("/employees", methods=["GET"])
def allCustomers():
    cur = db_conn.cursor()
    jobTitle = request.args.get("jobTitle")
    reportsTo = request.args.get("reportsTo")
    print("jobTitle", jobTitle)
    print("reportsTo", reportsTo)

    cur.execute(f"SELECT * FROM employees where jobTitle = '{jobTitle}'")
    # cur.execute("SELECT * FROM employees where reportsTo =1088 and jobTitle = 'Sales Rep'")
    return jsonify(cur.fetchall())

# http://localhost:3000/employees?jobTitle=Sales%20Rep%20%27%20OR%20%271=1%27
# obTitle=Sales Rep ' OR '1=1'

# ='Sales Rep'  OR 1=1 --
# = " 'Sales Rep' '1=1"
#  input => Sales Rep ' OR '1=1
app.run(
    debug=True, 
    host="localhost",
    port=3000
)



import db
from query import *
import json

db_conn = db.mysqlconnect()

# add_category
list_of_categories:Category =[
 Category("Electronics","All electronic items"),
 Category("Medicine","All medicine items"),
    Category("Clothing","All clothing items"),
    Category("Grocery","All grocery items"),
    Category("Books","All books items")

 ]

try:
    for category in list_of_categories:
        add_category(db_conn,category)
    print("Categories added")
except Exception as e:
    print(e)



# get all categories
categories = get_categories(db_conn)
print(
  "\n ** Getting All categories ** \n",
)
print(
  json.dumps(categories, default=str, indent=4)
)


# add_product
list_of_products:Product =[
 Product("Laptop",1,50000,"Dell Laptop",10,4.5),
 Product("Mobile",1,20000,"Samsung Mobile",20,4.0),
 Product("Tablet",1,10000,"Lenovo Tablet",30,3.5),
 Product("Pain Killer",2,100,"Crocin",100,4.0),
 Product("Panadol",2,50,"Paracetamol",200,4.5),
 Product("Polo Shirt",3,500,"White Shirt",100,4.0),
 Product("Jeans",3,1000,"Blue Jeans",200,4.5),
 Product("Mughal Rice",4,50,"Basmati Rice",100,4.0),
 Product("Wheat",4,40,"Whole Wheat",200,4.5),
 Product("Python Book",5,500,"Python Programming",100,4.0),
 Product("Dart Book",5,1000,"Dart Programming",200,4.5)
]

try:
    for product in list_of_products:
        add_product(db_conn,product)
    print("Products added")

except Exception as e:
    print(e)

# get all products
products = get_products(db_conn)
print(
  "\n ** Getting All products ** \n",
)
print(
    json.dumps(products, default=str, indent=4)
)

# add_user
list_of_users:User =[
 User("Amjad","amjad@gmail.com","123","Karachi","Karachi","Pakistan","123456"),
    User("Ali","ali123@gmail.com","123","Lahore","Lahore","Pakistan","123456"),
    User("Danish","dasnish@gmail,.com","123","Islamabad","Islamabad","Pakistan","123456"),
]

try:
    for user in list_of_users:
        add_user(db_conn,user)
    print("Users added")

except Exception as e:
    print(e)

# get all users
users = get_users(db_conn)
print(
  "\n ** Getting All users ** \n",
)
print(
    json.dumps(users, default=str, indent=4)
)


# add order
list_of_orders:Order =[
 Order(1,1,1,1,50000),
 Order(1,1,1,1,50000),
 Order(2,2,2,2,20000),
 Order(3,3,3,3,10000),
]
      
      


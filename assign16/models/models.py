# user class

class User:
    name = ""
    email = ""
    pw = ""
    address = ""
    city = ""
    country = ""
    ph_no = ""

    def __init__(self, name,email,pw,address,city,country,ph_no):
        self.name = name
        self.email = email
        self.pw = pw
        self.address = address
        self.city = city
        self.country = country
        self.ph_no = ph_no

   

class Product:
    def __init__(self,name,category_id,price,desc,inventory_qty,avg_rating):
        self.name = name
        self.category_id = category_id
        self.price = price
        self.desc = desc
        self.inventory_qty = inventory_qty
        self.avg_rating = avg_rating


class Category:
    # name = ""
    # desc = ""
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc

class Order:
    def __init__(self,user_id,date,status,shipping_address,shipping_city,shipping_country,total_amount):
        self.user_id = user_id
        self.date = date
        self.status = status
        self.shipping_address = shipping_address
        self.shipping_city = shipping_city
        self.shipping_country = shipping_country
        self.total_amount = total_amount

    
class OrderDetail:
    def __init__(self,order_id,product_id,quantity,price):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price





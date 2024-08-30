import pymysql

from assign16.models.models import *

def getFromDB(db_conn: pymysql.Connection, query: str):
  cur = db_conn.cursor()
  cur.execute(query)
  return cur.fetchall()

def postToDB(db_conn: pymysql.Connection, query: str):
    cur = db_conn.cursor()
    cur.execute(query)
    db_conn.commit()


#################### Category Related Queries ####################
def add_category(db_conn: pymysql.Connection,data:Category):
  query=f"""
      insert into category 
      values (
        {data.name},
        '{data.desc}',        
      )
    """
  postToDB(db_conn,query)

def get_categories(db_conn: pymysql.Connection):
    query = "select * from category"
    return getFromDB(db_conn, query)

#################### Product Related Queries ####################
def add_product(db_conn: pymysql.Connection,data:Product):
  query=f"""
      insert into product 
      values (
        {data.name},
        {data.category_id},
        {data.price},
        '{data.desc}',
        {data.inventory_qty},
        {data.avg_rating}
      )
    """
  postToDB(db_conn,query)

def get_products(db_conn: pymysql.Connection):
    query = "select * from product"
    return getFromDB(db_conn, query)

#################### User Related Queries ####################
def add_user(db_conn: pymysql.Connection,data:User):
  query=f"""
      insert into user 
      values (
        {data.name},
        {data.email},
        {data.pw},
        {data.address},
        {data.city},
        {data.country},
        {data.ph_no}
      )
    """
  postToDB(db_conn,query)

def get_users(db_conn: pymysql.Connection):
    query = "select * from user"
    return getFromDB(db_conn, query)

#################### Order Related Queries ####################

def add_order(db_conn: pymysql.Connection,data:Order):
    query=f"""
        insert into order 
        values (
            {data.user_id},
            {data.date},
            {data.status},
            {data.shipping_address},
            {data.shipping_city},
            {data.shipping_country},
            {data.total_amount}
        )
        """
    postToDB(db_conn,query)

def get_orders(db_conn: pymysql.Connection):
    query = "select * from order"
    return getFromDB(db_conn, query)

#################### OrderDetail Related Queries ####################
def add_order_detail(db_conn: pymysql.Connection,data:OrderDetail):
    query=f"""
        insert into order_detail 
        values (
            {data.order_id},
            {data.product_id},
            {data.quantity},
            {data.price}
        )
        """
    postToDB(db_conn,query)

def get_order_details(db_conn: pymysql.Connection):
    query = "select * from order_detail"
    return getFromDB(db_conn, query)


# Statistics Queries
def salesMetrics(db_conn: pymysql.Connection):
    query = """
    select sum(total_amount) as total_sales, avg(total_amount) as avg_sales from order
    """
    return getFromDB(db_conn, query)

def orderMetrics(db_conn: pymysql.Connection):
    query = """
    select count(*) as total_orders from order
    """
    return getFromDB(db_conn, query)

def paymentMetrics(db_conn: pymysql.Connection):
    query = """
    select sum(total_amount) as total_payment from order
    """
    return getFromDB(db_conn, query)

def productMetrics(db_conn: pymysql.Connection):
    query = """
    select count(*) as total_products from product
    """
    return getFromDB(db_conn, query)

def bestSellingProduct(db_conn: pymysql.Connection):
    query = """
    select id, sum(quantity) as total_quantity from order_detail group by product_id order by total_quantity desc limit 1
    """
    return getFromDB(db_conn, query)

def graphicalMetrics(db_conn: pymysql.Connection):
    query = """
    select product_id, sum(quantity) as total_quantity from order_detail group by product_id
    """
    return getFromDB(db_conn, query)
  
  
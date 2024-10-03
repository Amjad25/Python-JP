import pymysql
 
def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password="amjad@123", 
        db='notes_app',
        cursorclass=pymysql.cursors.DictCursor,
    )
    print("db connected")
    return conn
    

def disconnect(conn: pymysql.Connection):
  conn.close()


if __name__ == "__main__":
    mysqlconnect()
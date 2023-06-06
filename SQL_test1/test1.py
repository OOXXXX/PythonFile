import mysql.connector

# 连接到数据库
mydb = mysql.connector.connect(
  host="localhost",
  user="root",  # 替换为你的用户名
  password="zhupx780512",  # 替换为你的密码
  database="mydatabase"  # 替换为你的数据库名
)

# 创建一个游标
mycursor = mydb.cursor()

# 创建一个新表
# mycursor.execute("""
# CREATE TABLE customers (
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   name VARCHAR(255),
#   address VARCHAR(255)
# )
# """)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()


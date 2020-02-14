import connect

cursor = db.cursor()
cursor.execute("CREATE DATABASE if not exists toko_mainan")
print("Database berhasil dibuat!")

sql = """CREATE TABLE if not exists customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel customers berhasil dibuat!")

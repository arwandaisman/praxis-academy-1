import connect

cursor = connect.db.cursor()
sql = """CREATE TABLE if not exists members (
  member_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address Varchar(255),
  salutation_id int
)
"""
cursor.execute(sql)
print("Tabel members berhasil dibuat!")

sql = """CREATE TABLE if not exists rent_mv (
  rent_id INT AUTO_INCREMENT PRIMARY KEY,
  member_id int,
  movie_rent VARCHAR(255)
)
"""
connect.cursor.execute(sql)
print("Tabel Rent Movie berhasil dibuat!")

sql = """CREATE TABLE if not exists salutation (
  salutation_id INT AUTO_INCREMENT PRIMARY KEY,
  salutation VARCHAR(10)
)
"""
connect.cursor.execute(sql)
print("Tabel salutaion berhasil dibuat!")
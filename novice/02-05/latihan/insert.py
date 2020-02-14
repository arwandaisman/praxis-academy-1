import connect 

cursor = connect.db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Dian", "Mataram")
cursor.execute(sql, val)

connect.db.commit()

print("{} data ditambahkan".format(cursor.rowcount))

print("insert dengan perulangan")
values = [
  ("Doni", "Jakarta"),
  ("Ella", "Surabaya"),
  ("Fani", "Bandung"),
  ("Galih", "Depok")
]

for val in values:
  cursor.execute(sql, val)
  connect.db.commit()

print("{} data ditambahkan".format(len(values)))
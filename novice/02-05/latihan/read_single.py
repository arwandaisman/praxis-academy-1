import connect

cursor = connect.db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)

result = cursor.fetchone()

print(result)
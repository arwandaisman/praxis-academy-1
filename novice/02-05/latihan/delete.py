import connect

cursor = connect.db.cursor()
sql = "DELETE FROM customers WHERE customer_id=%s"
val = (2,)
cursor.execute(sql, val)

connect.db.commit()

print("{} data dihapus".format(cursor.rowcount))
import connect

cursor = connect.db.cursor()
sql = """select members.name,rent_mv.movie_rent from rent_mv,members where members.name="Janet Jones" AND rent_mv.member_id=1"""
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)
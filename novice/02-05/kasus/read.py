import connect

cursor = connect.db.cursor()
#sql = """select members.name,rent_mv.movie_rent from rent_mv,members where members.name="Janet Jones" AND rent_mv.member_id=1"""
sql= "select member_id from members where member_id=1"
cursor.execute(sql)

results = cursor.fetchall()


for data in results:
  a = str(data).replace('(','').replace(',','').replace(')','')
  #print(data)

print(a)

sql2="select rent_mv.movie_rent from rent_mv where rent_mv.member_id={}".format(a)
cursor.execute(sql2)

result = cursor.fetchall()
print(result)

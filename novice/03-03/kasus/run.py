from flask import Flask, render_template, request, url_for
from markupsafe import escape
import mysql.connector as mariadb
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():

    conn = mariadb.connect(
        host="localhost",
        user="root",
        passwd="123",
        database='rental'
    )

    cur = conn.cursor()

    sql = "SELECT * FROM members"
    cur.execute(sql)
    results = cur.fetchall()
    data=[]
    for i in results:
        data.append(i)
    return render_template(
        'home.html', my_string="Welcome home!", title="Home", data=data)

@app.route("/insert")
def insert():
    return render_template(
        'insert.html', my_string="Let's insert some data!",
        title="Insert")

@app.route("/update/<int:idmember>")
def update(idmember):
    conn = mariadb.connect(
        host="localhost",
        user="root",
        passwd="123",
        database='rental'
    )

    cur = conn.cursor()
    sql = "Select * from members where member_id='{}'".format(idmember)
    cur.execute(sql)
    results = cur.fetchall()
    data=[]
    for i in results:
        data.append(i)
    return 'asd %d' % idmember
    return render_template(
        'update.html', my_string="You can also update your data directly.", title=a, data=data)


@app.route("/actupdate", methods=['GET', 'POST'])
def actupdate():
    if (request.method == 'POST'):
        try:
            name=request.form['name']
            address=request.form['address']
            conn = mariadb.connect(
                host="localhost",
                user="root",
                passwd="123",
                database='rental'
            )

            cur = conn.cursor()
            sql = "UPDATE members set name='{}', address='{}' where member_id=1".format(name,address)
            cur.execute(sql)
            conn.commit()
            return render_template(
                'msg.html', my_string="Data Has Been Stored.", title="Insert")
        except:
            return render_template(
                'msg.html', my_string="Databases Connection Error!", title="Insert")

@app.route("/act", methods=['GET', 'POST'])
def act():
    if (request.method == 'POST'):
        try:
            name=request.form['name']
            address=request.form['address']
            conn = mariadb.connect(
                host="localhost",
                user="root",
                passwd="123",
                database='rental'
            )

            cur = conn.cursor()
            sql = "INSERT INTO members(name,address) VALUES ('{}','{}')".format(name,address)
            cur.execute(sql)
            conn.commit()
            return render_template(
                'msg.html', my_string="Data Has Been Stored.", title="Insert")
        except:
            return render_template(
                'msg.html', my_string="Databases Connection Error!", title="Insert")

if __name__ == '__main__':
    app.run(debug=True)

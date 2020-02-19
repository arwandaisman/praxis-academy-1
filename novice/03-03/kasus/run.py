from flask import Flask, render_template
import mysql.connector as mariadb
app = Flask(__name__)



@app.route("/")
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

# @app.route("/home")
# def home():
#     return render_template(
#         'home.html', my_string="Welcome home!", title="Home")

@app.route("/insert")
def insert():
    return render_template(
        'template.html', my_string="Let's insert some data!", 
        my_list=[0,1,2,3,4,5], title="Insert")

@app.route("/update")
def update():
    return render_template(
        'template.html', my_string="You can also update your data directly.", 
        my_list=[0,1,2,3,4,5], title="Update")

if __name__ == '__main__':
    app.run(debug=True)

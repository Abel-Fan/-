from flask import Flask,render_template,request,redirect
import pymysql
db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password='123456',
    database="yd1",
)

app = Flask(__name__)

@app.route("/")
def index():
    cursor = db.cursor()
    sql = "select * from goods"
    cursor.execute(sql)
    datas = cursor.fetchall()
    print(datas)
    return render_template("index.html")
@app.route("/addgoods",methods=['POST','GET'])
def add():

    if request.method =="POST":
        title1 = request.form['title1']
        title2 = request.form['title2']
        info = request.form['info']
        price = request.form['price']
        img = request.files['img']
        f = request.files['img']
        filename = "static/upload/"+f.filename
        f.save(filename)
        cursor = db.cursor()
        cursor.execute("insert into goods (title,title2,info,price,img) values ('%s','%s','%s',%s,'%s')"%(title1,title2,info,price,filename))
        db.commit()
        return redirect("/addgoods")
    else:
        return render_template("addgoods.html")

if __name__ == "__main__":
    app.run(debug=True)
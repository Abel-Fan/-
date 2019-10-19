from flask import Flask,render_template,request,redirect
import pymysql
# 实例化web服务器
app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="yd2"
)


# 创建首页的路由
@app.route("/")
def index():
    cursor = db.cursor()
    sql = "select * from goods"
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template("index.html",data=data)

# 创建后台的路由
@app.route("/admin")
def admin():
    cursor = db.cursor()
    sql = "select * from goods"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    return render_template("admin.html",data=data)

@app.route("/addgoods",methods=['POST'])
def addgoods():
    title = request.form['title']
    title2 = request.form['title2']
    info = request.form['info']
    price = request.form['price']
    file = request.files['img']
    filename = "static/upload/"+file.filename
    file.save(filename)
    print(title,title2,info,price)

    # 创建游标
    cursor = db.cursor()
    sql = "insert into goods (title,title2,info,price,img) values ('%s','%s','%s','%s','%s')"%(title,title2,info,price,filename)
    cursor.execute(sql)
    db.commit()

    # 重定向
    return redirect("/admin")


if __name__ == "__main__":
    app.run(debug=True)

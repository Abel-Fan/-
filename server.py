from flask import Flask,render_template,request
import pymysql
# 实例化web服务器
app = Flask(__name__)
# 创建首页的路由
@app.route("/")
def index():
    return render_template("index.html")

# 创建后台的路由
@app.route("/admin")
def admin():
    return render_template("admin.html")

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
    return "1"


if __name__ == "__main__":
    app.run(debug=True)

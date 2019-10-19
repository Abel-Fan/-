from flask import Flask,render_template

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



if __name__ == "__main__":
    app.run(debug=True)

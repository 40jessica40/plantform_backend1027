from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "hello world"

# 加载页面，在页面中请求上方的hello接口
@app.route("/kuayu_demo")
def kuayu_demo():
    return render_template("kuayu_demo.html")


@app.route("/cors_demo")
def cors_demo():
    return render_template("cors_demo.html")


if __name__ == '__main__':
    app.run(debug=True)
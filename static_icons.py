from flask import Flask, render_template, Blueprint

app = Flask(__name__)

static_router = Blueprint(name="static_usage", import_name=__name__, url_prefix="/static_usage")

# 1、 生成静态文件 URL
# <img src="{{ url_for('static', filename='pic.jpg') }}">

@static_router.route("/png/")
def static_png():
    return render_template("static_icon.html")
# 2、添加图标
# 图标（favourite icon） 是显示在标签页和书签栏的网站头像。需要准备一个 ICO、PNG 或 GIF 格式的图片，大小一般为 16×16、32×32、48×48 或 64×64 像素。把这个图片放到 static 目录下，然后在 HTML 模板里引入它。
@static_router.route("/icon/")
def static_icon():
    return render_template("static_icon.html")

# 3、添加图片
# 可以在 static 目录下面创建一个子文件夹 images，把图片都放到这个文件夹里。
# 创建子文件夹并不是必须的，只是为了更好的组织同类文件。同样的，如果有多个 CSS 文件，也可以创建一个 css 文件夹来组织他们。
@app.route("/picture/")
def static_picture():
    return render_template("static_icon.html")




# 4.添加图片
# 第一步：准备css文件
@app.route("/css_style/")
def static_css():
    return render_template("static_icon.html")


if __name__ == '__main__':
    app.register_blueprint(static_router)
    app.run(port=5052, debug=True)

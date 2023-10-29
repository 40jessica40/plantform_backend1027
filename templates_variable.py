# from flask import Flask, Blueprint, render_template
# app = Flask(__name__)
# #初始化蓝图对象
#
# template_router = Blueprint(name="template", import_name=__name__, url_prefix="/template")
#
# #定义路由
# @template_router.route("/variable")
# def variable():
#     return render_template("variable.html", title="模板语法", content="通过render_template()方法传递值到模板文件")


from flask import Flask, Blueprint, render_template

# 初始化服务对象
app = Flask(__name__)
# 初始化蓝图对象
template_router = Blueprint(name="template",import_name=__name__,url_prefix="/template")

# 定义路由
@template_router.route("/variable")
def variable():
    # 返回模板文件，并且将值传递给模板文件
    return render_template("variable.html", title="模板语法", content="通过render_template()方法将值传递到模板文件~~")


if __name__ == '__main__':
    # 注册蓝图
    app.register_blueprint(template_router)
    # debug模式启动服务
    app.run(port=5050, debug=True)

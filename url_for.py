# url_for() 的用法
# url_for() 可以根据视图函数名生成视图的路由地址。
#
# 语法：url_for(视图函数名, *）
#
# 视图地址：str 类型，可以是视图函数名，也可以是由蓝图和视图函数组成的地址。
# *：允许传递参数。
# 用法：
#
# 用法一：url_for(视图函数名)
# 用法二：url_for("蓝图名.视图函数名")
#
# （1）用法一：url_for(视图函数名)
# 使用 url_for(视图函数名) 即可返回对应视图函数的 url。

# """
# url_for(视图名)，获取到该视图的path
# """
# from flask import Flask, url_for
#
# app = Flask(__name__)
#
# @app.route("/login/")
# def login():
#     # url_for(视图名)，获取到该视图的path
#     return url_for("account")
#
# @app.route("/account/")
# def account():
#     return "我的账户页面"

#
#
# if __name__ == '__main__':
#     app.run(debug=True)



# （2）用法二：url_for("蓝图名.视图函数名")
"""
url_for("蓝图名.视图名")，获取对应视图的path
"""
from flask import Flask, Blueprint, url_for

app = Flask(__name__)

# 定义两个视图
login_router = Blueprint(name="login_module",import_name=__name__,url_prefix='/login')
cart_router = Blueprint(name="cart_module",import_name=__name__,url_prefix="/cart")

# 登录视图
@login_router.route("")
def login():
    return url_for("cart_module.cart")

@cart_router.route("")
def cart():
    return "进入购物车"

if __name__ == '__main__':
    app.register_blueprint(login_router)
    app.register_blueprint(cart_router)
    app.run(port=5050, debug=True)


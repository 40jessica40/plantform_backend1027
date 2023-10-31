"""
4、 路由跳转(重定向)
重定向（Redirect）就是通过各种方法将各种网络请求重新定个方向转到其它位置。可以在生成视图的路由地址后，使用 redirect() 方法实现路由的跳转。

redirect() 使得一个路由地址 A 与另一个路由地址 B 联系起来，执行 A 的时候会跳转执行 B。

语法：flask.redirect(location, code=302, Response=None)

location 是一个链接地址，可以使用 url_for() 函数得到，也可以是静态文件地址。
code HTTP 协议中的一个状态码。
Response 是一个响应类。
用法：

用法一：redirect(url地址)
用法二：redirect(路由地址)(可以结合 url_for 使用)"""


#（1）用法一：redirect(url地址)
# redirct(url)跳转到给定的url

#
# from flask import Flask, request, redirect
# app = Flask(__name__)
#
#
# @app.route("/login/")
# def login():
#     args = request.args
#     username = args.get("username")
#     password = args.get("password")
#     print(type(username))
#     print(type(password))
#     # 判断是否登录成功-如果登录成功就进行跳转
#     # get相应的ttp://127.0.0.1:5050/login/?username=tangbohu&&password=9527
#     if username == "tangbohu" and password == "9527":
#         return redirect("https://www.baidu.com/")
#     else:
#         return f"username={username}-类型{type(username)},password={password}-类型{type(password)},用户名或密码错误！"

#（2） 用法二：redirect(路由地址)(可以结合 url_for 使用)

"""
redirect(路由)，跳转到对应的路由视图
"""
"""
redirect(路由)，跳转到对应的路由视图
"""
from flask import Flask, Blueprint, request, redirect, url_for

app = Flask(__name__)

# 初始化两个蓝图
login_router = Blueprint(name="login_module", import_name=__name__,url_prefix="/login")
cart_route = Blueprint(name="cart_module", import_name=__name__,url_prefix="/cart")


@login_router.route("/")    # 一定记得要加/，避免访问的时候的路径问题
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username == "tangbohu" and password == "9527":
        # 如果登录成功，则跳转到购物车列表页面
        return redirect(url_for("cart_module.cart_list"))
    else:
        return "用户名或密码错误！"


@cart_route.route("/list/")
def cart_list():
    cart_list = {
        "code":0,
        "errmsg":"success",
        "cart_list":["鞋子","袜子","鞋垫"]
    }
    return cart_list


if __name__ == '__main__':
    app.register_blueprint(login_router)
    app.register_blueprint(cart_route)
    app.run(port=5050, debug=True)




















if __name__ == '__main__':
    app.run(port=5050, debug=True)


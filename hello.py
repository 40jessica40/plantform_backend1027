import logging

from flask import Flask, request, jsonify, render_template, make_response, Blueprint
from werkzeug.utils import secure_filename

from log_util import logger

app = Flask(__name__)

# 二、接口路由技术

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hoggeder/<int:username>')
def hoggede(username):
    logger.info(f'这是{username}的个人信息')
    logging.info("111111111")
    return f'这是{username}的个人信息'


@app.route('/demo3/<float:float_content>', methods=['get'])
def demo(float_content):
    return f'这是{float_content}的信息'


@app.route('/demo4/<string:string_content>', methods=['get'])
def demo4(string_content):
    return f'这是{string_content}的信息'


@app.route('/demo5/<path:path1>', methods=['get'])
def demo5(path1):
    return f'这是{path1}的信息'

# 规范的URL： 路由的尾部使用斜杠 （/）；

# 三、请求方法与处理请求数据
@app.route("/get/<int:id>")
def get_data_01(id):
    return f'通过id = {id}获取数据，get_data_01'


@app.route("/get/<int:id>", methods=['get'])
def get_data_02(id):
    return f'通过id = {id}获取数据，get_data_01'


@app.route('/post/<string:name>/<int:id>', methods=['post'])
def post_data_01(name, id):
    return f'通过id={id}，name={name}来创建或者更新需求'


@app.route('/put/<string:name>/<int:id>', methods=['put'])
def put_data_01(name, id):
    return f'通过id={id}，name={name}来创建或者更新需求'

# 3、处理请求数据
#(1)flask中request对象
# args	记录请求中的查询参数	字典格式，get请求url拼接的query参数
# json	记录请求中的 json 数据	字典格式，post或者put请求中发送的JSON格式数据
# files	记录请求上传的文件	字典格式，每个上传的文件都会存储在这个字典里
# form	记录请求中的表单数据	字典格式，post请求发送的form格式数据
# method	记录请求使用的 HTTP 方法
# url	记录请求的 URL 地址
# host	记录请求的域名
# headers	记录请求的头信息
# 1.get请求参数处理
# 如果一个 GET 请求在 URL 中拼接了请求参数，可以使用 request.args 来获取 GET 请求中携带的请求参数。request.args 是一个字典，可以通过键名来获取参数的值。
# get请求query处理

#（2）get请求参数处理
@app.route("/getinfo/")
def get_request_args():
    # 获取请求url中携带的参数
    url_params = request.args
    # 从请求参数中获取id
    id = url_params.get("id")

    # request中的属性值
    header_items = request.headers.items()
    print(f"request.headers--value={header_items}")
    # items是一个生成器
    print(f"request.headers--type={type(header_items)}")
    # 将request.headers.items()中的数据转字典
    header_json = {}
    for header in header_items:
        # header是一个元组
        print("header------------>", header)
        key = header[0]
        header_json[key] = header[1]

    host = request.host
    host_url = request.host_url
    method = request.method
    base_url = request.base_url
    path = request.path
    values = request.values
    # request.values=CombinedMultiDict([ImmutableMultiDict([])])
    print(f"request.values={values}")
    # 转换成字符串进行返回
    result = {"request.args":url_params,
                        "从请求参数中获取id":id,
                        "request.host":host,
                        "request.host_url":host_url,
                        "request.method":method,
                        "request.base_url":base_url,
                        "request.path":path,
                        "request.headers.items()转字典":header_json
                        }

    return result

# （3）post请求form处理
@app.route("/postform/", methods=["POST"])
def post_request_form():
    form = request.form
    return {"服务端获取到的表单数据": form}

# （4） post请求json处理
@app.route("/postjson", methods=["post"])
def post_request_json():
    json = request.json
    return {"服务端收到的json数据": json}

# （5） post请求file处理
"""可以使用 request.files 来获取请求中包含的文件。request.files 是一个字典，每个上传的文件都会存储在这个字典里。可以通过 file 这个 key 来获取其中的文件对象。

已上传的文件存储在内存或是文件系统中一个临时的位置。它有一个 save() 方法，这个方法允许把文件保存到服务器的文件系统上。

如果想知道上传前文件在客户端的文件名是什么，可以访问 filename 属性。但这个值是可以伪造的。如果要把文件按客户端提供的文件名存储在服务器上，需要把它传递给 Werkzeug 提供的 secure_filename() 函数。这个函数可以用来确保文件名是安全的。"""


@app.route("/postfiles", methods=["post"])
def post_request_files():
    files = request.files
    print(type(files))  # <class 'werkzeug.datastructures.structures.ImmutableMultiDict'>
    print(files)  # ImmutableMultiDict([('new_pic_name', <FileStorage: 'shootup.png' (None)>)])
    # 通过文件名获取上传的文件
    file = files.get("img.png")
    # 使用save()方法把文件保存到本地--需要提前创建存放文件的目录，使用secure_filename() 函数确保文件名安全
    file.save("../uploads" + secure_filename(file.filename))  # save有两个参数，一个是路径+文件名，另一个是buffer_size

    return f"你上传的真实文件名是不是{secure_filename(file.filename)}？"


@app.route("/putjson", methods=["put"])
def put_request_json():
    json = request.json
    return {"服务端收到的json数据": json}






"""四、处理响应数据
使用Flask的视图函数的return给客户端返回响应信息；

1、 接口响应常见类型
文本型：直接return字符串；
元组：返回多个值，但是排列有讲究，第一个是Response对象(也就是响应体信息)，第二个是status_code(如果不写默认就是200)，第三个是响应头信息；Response为必选项，其他两个任意；
JSON：JSON格式的响应体信息；
HTML：html格式的响应体信息；
额外数据：其他响应信息，比如cookie等；
（1） 返回文本类型
返回文本类型比较简单，直接在视图函数返回字符串即可；
特点就是返回的Headers中默认会返回响应类容格式：Content-Type：text/html; charset=utf-8；
（2） 返回元组类型
元组格式包含 3 个参数类型。第一个是 response 对象，第二个是响应状态码，第三个是响应头信息。也可以只填写 2 个返回信息，但是Response为必选项。比如 (response, status) 结合，还有 (response, headers) 结合。
（3）返回json类型
第一种是使用 jsonify() 方法，此方法支持，直接传入一个字典，也支持通过关键字参数传递。
第二种方法就是直接返回字典，在 Flask 1.1 版本之后，直接返回 python 的字典类型时，Flask 会调用 jsonify() 方法。
4）返回HTML
返回 HTML 主要使用的是模板渲染技术。
方法：render_template(html文件名)；
注意：注意html文件必须在 templates 目录下，templates目录名称固定不变，并且在“app”py文件的同级目录下；"""


@app.route("/tuple/")
def response_tuple():
    return {"content":"这是响应体信息"},200,{"my_header":"private_header"}

@app.route("/json/")
def response_json_01():
    return {"content":"直接返回json信息","type":1}

@app.route("/jsonify_dict/")
def response_json_02():
    return jsonify({"content":"通过传递字典给jsonify返回json","type":2})

@app.route("/jsonify_key_value/")
def response_json_03():
    return jsonify(content="通过给jsonify传递键值对方式返回json", type=3)


@app.route("/index_html/")
def response_html():
    # 调用render_template方法，传入html 文件的名称。
    # 注意html文件必须在 templates 目录下
    return render_template("qq.html")


"""
（5） 返回额外数据
可以返回更多响应字段类容，比如：文件格式、文件语言、文件大小、cookie、headers等；
方法：使用make_response(render_template('文件名'))得到一个Response对象，通过对象去设置响应的返回字段内容；"""


@app.route("/response_other")
def response_other():
    # 调用render_template方法，传入html 文件的名称。注意html文件必须在 templates 目录下
    # 创建一response对象
    response = make_response(render_template("qq.html"))
    # 设置cookie
    response.set_cookie('cookies_key', 'cookies_content')
    # 设置响应头
    response.headers["myheader"] = 'private_header'
    # 设置响应数据类型
    response.content_type = 'multipart/form-data'
    # 设置响应类容语言
    response.content_language = 'html'

    return response


# 五、服务主机端口配置及debug模式

# 六、蓝图与视图
# 要使用蓝图，首先要声明一个蓝图对象。

goods_router = Blueprint(name="goods", import_name=__name__)
user_router = Blueprint(name="users", import_name=__name__, url_prefix="/user")


@goods_router.route("/rr")
def index():
    return {"code":0, "msg": "get success", "data": []}


@goods_router.route("/add/", methods=["POST"])
def add_goods():
    return {"code":0, "msg": "add success"}


@user_router.route("/add/", methods=["post"])
def add_users():
    return {"code":0, "msg": "add user success"}

# 七、模板技术







if __name__ == "__main__":
    app.register_blueprint(goods_router)
    app.register_blueprint(user_router)
    app.run(debug=True)


from flask import Flask, render_template, Blueprint

app = Flask(__name__)
template_router = Blueprint(name="template", import_name=__name__, url_prefix="/template")


# @template_router.route("/single/")
# def template_include_single():
#     return render_template("son_include_single.html",content="导入单个文件",money=200)


@template_router.route("/son_include_list/")
def template_include_list():
    return render_template("son_include_list.html",content="导入模板列表",money=300)


if __name__ == '__main__':
    app.register_blueprint(template_router)
    app.run(port=5050, debug=True)
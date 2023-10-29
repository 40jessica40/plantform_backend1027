from flask import Flask, render_template, Blueprint

template_router = Blueprint(name="template", import_name=__name__, url_prefix="/template")

app = Flask(__name__)
@template_router.route("/for_endfor/")
def for_endfor():
    # 列表
    money = [50,90,100,102,180,75,900]
    # 字典
    person_dict = [
        {
            "name": "张三",
            "money": 100000000
        },
        {
            "name": "李四",
            "money": 1000
        },
        {
            "name": "王五",
            "money": 1000
        },
    ]
    return render_template("for_endfor.html",money_list=money,person=person_dict,content="循环语句")


if __name__ == '__main__':
    app.register_blueprint(template_router)
    app.run(port=5050, debug=True)

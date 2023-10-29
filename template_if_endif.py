from flask import Flask, render_template, Blueprint

# from templates_variable import template_router
# from L2.templates_usage.templates_variable import template_router

template_router = Blueprint(name="template", import_name=__name__, url_prefix="/template")
app = Flask(__name__)

@template_router.route("/if_endif/")
def if_endif():
    person_data = {
        "name":"张三",
        "money":1000000,
        "gender":"男"
    }
    return render_template("if_endif.html", person=person_data, title="模板语法", other="其实你也长得很漂亮")


if __name__ == '__main__':
    app.register_blueprint(template_router)
    app.run(port=5050, debug=True)


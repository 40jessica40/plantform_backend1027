from flask import Flask, Blueprint, render_template

app = Flask(__name__)
template_router = Blueprint(name="template", import_name=__name__, url_prefix="/template")


@template_router.route("/parent")
def template_parent():
    return render_template("parent.html", title="父模板title", content="父模板content",footer="父模板footer")


@template_router.route("/son")
def template_son():
    return render_template("son.html", title="子模板title", content="子模板content",money=1000)


if __name__ == '__main__':
    app.register_blueprint(template_router)
    app.run(port=5050, debug=True)
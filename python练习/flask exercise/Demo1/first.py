from flask import Flask, render_template, request, session, redirect, url_for
from ser.user import user_blue
import setting

app = Flask("__name__", template_folder="ser_templates", static_folder="static", static_url_path="/static")
app.secret_key = "md5python"
app.session_cookie_name = "hello"

# 查看默认配置
# app.config    make_config     default_config
app.config.from_object(setting.Debug)
app.register_blueprint(user_blue)


def outer(func):
    def inner(*args, **kwargs):
        if session.get("user"):
            ret = func(*args, **kwargs)
            return ret
        else:
            return redirect("/login")

    return inner


@app.route("/<nid>/<nid2>", endpoint="index")
# @outer
def index(nid, nid2):
    print(nid, nid2)
    # print(url_for("index"))
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        session["user"] = request.form.get("username")
        return redirect("/<nid>/<nid2>")


@app.route("/detail", endpoint="detail")
@outer
def detail():
    return render_template("detail.html")



app.run(debug=True)

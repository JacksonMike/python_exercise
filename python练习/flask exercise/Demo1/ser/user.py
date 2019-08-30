from flask import Blueprint, render_template

#  蓝图实列对象
user_blue = Blueprint("user", __name__, template_folder="ser_templates", url_prefix="/user")


# http://127.0.0.1:5000/user/user_login
@user_blue.route("/user_login")
def user_login():
    return render_template("index2.html")

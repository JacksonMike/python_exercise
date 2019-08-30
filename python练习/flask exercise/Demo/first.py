import json

from flask import Flask, render_template, redirect, jsonify, send_file, request, Markup, session

app = Flask(__name__)
app.secret_key = "Jim"
STUDENT = {'name': 'Old', 'age': 38, 'gender': '中'}

STUDENT_LIST = [
    {'name': 'Old', 'age': 38, 'gender': '中'},
    {'name': 'Boy', 'age': 73, 'gender': '男'},
    {'name': 'EDU', 'age': 84, 'gender': '女'}
]

STUDENT_DICT = {
    1: {'name': 'Old', 'age': 38, 'gender': '中'},
    2: {'name': 'Boy', 'age': 73, 'gender': '男'},
    3: {'name': 'EDU', 'age': 84, 'gender': '女'}
}


@app.route("/")
def index():
    # return jsonify({"name": "Jim", "age": 99})
    return send_file("first.py")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        print(request.values.to_dict())
        # picture = request.files.get("file")
        # picture.save(picture.filename)
        user_info = request.form.to_dict()
        if user_info.get("username") == "Jim" and user_info.get("pwd") == "123":
            session["user"] = "Jim"
            return redirect("/mall")
        return render_template("login.html", msg="用户名或者密码错误")


# session
@app.route("/mall")
def mall():
    if session.get("user"):
        return render_template("mall.html", user=session.get("user"))


@app.route("/student")
def student():
    return render_template("student.html", s=STUDENT)


@app.route("/lst")
def lst():
    return render_template("student_list.html", student=STUDENT_LIST)


@app.route("/dic")
def dic():
    return render_template("student_dict.html", s=STUDENT_DICT)


@app.route("/safe")
def safe():
    tag = Markup("<input type='text'>")
    tag2 = "<input type='text'>"
    return render_template("safe.html", tag=tag, tag2=tag2)


def sum_num(a, b):
    return a + b


@app.route("/func")
def func():
    return render_template("func.html", tag=sum_num)


# 全局函数
@app.template_global()
def mul_num(a, b):
    return a * b


# 三个参数
@app.template_filter()
def three_num(a, b, c):
    return a * b * c


@app.route("/inherit")
def inherit():
    return render_template("inherit.html")


app.run(host="127.0.0.1", port=5000, debug=True)

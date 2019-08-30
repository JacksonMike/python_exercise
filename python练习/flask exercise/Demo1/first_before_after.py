from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)
app.secret_key = "hello"


@app.before_request
def is_login():
    print("be1")
    if request.path == "/login":
        return None
    if session.get("user"):
        return None
    else:
        return redirect("/login")


@app.before_request
def be2():
    print("be2")
    return None


@app.before_request
def be3():
    print("be3")
    return None


@app.after_request
def af3(res):
    print("af3")
    return res


@app.after_request
def af2(res):
    print("af2")
    return res


@app.after_request
def af1(res):
    print("af1")
    return res


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        session["user"] = request.form.get("username")
        return redirect("/index")


@app.route("/index")
def index():
    return "Index"


@app.route("/home")
def home():
    return "Home"


# @app.after_request
# def foot_log(response):
#     print("af1")
#     if request.path != "/login":
#         print("有客人访问了", request.path)
#     return response


@app.errorhandler(404)
def error404(args):
    print(args)
    return "你访问的页面不存在%s" % args


app.run(debug=True)

from flask import Flask, views, url_for, render_template, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = "Jim"


@app.route('/')
def hello_world():
    flash("666", "tag")
    return 'Hello World!'


class LoginClass(views.MethodView):
    def get(self):
        print(url_for("login"))
        print(get_flashed_messages())
        return render_template("login.html")

    def post(self):
        return "hello"


app.add_url_rule("/login", view_func=LoginClass.as_view("login"))
app.run(debug=True)

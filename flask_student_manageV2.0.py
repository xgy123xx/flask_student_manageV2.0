from flask import Flask,render_template,request,session
from flask import views
from flask_session import Session
from register_forms import RegisterForm
from models import mysqlHandler
import redis
app = Flask(__name__)
app.secret_key = "helloworld"

# app.config["secret_key"] = "123123123"
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = redis.Redis(host="127.0.0.1",port=6379,db=1)
Session(app)

@app.route('/')
def hello_world():
    if not session.get("IS_LOGINED"):
        return "没有权限访问"
    return 'Hello World!'

class Login(views.MethodView):
    def get(self):
        return render_template("login.html")

    def post(self):
        user = request.form.get("username")
        passwd = request.form.get("password")
        print(user)
        print(passwd)
        if user == "alex" and passwd == "123":
            session["IS_LOGINED"] = "True"
            return "登录成功"
        else:
            msg = "用户名或密码错误"
            return render_template("login.html",msg=msg)
app.add_url_rule("/login",endpoint="login",view_func=Login.as_view(name="login"))

class Register(views.MethodView):
    def get(self):
        regfm = RegisterForm()
        return render_template("register.html",fm=regfm)

    def post(self):
        regfm = RegisterForm(request.form)
        print(request.form)
        if not regfm.validate():
             return render_template("register.html",fm=regfm)
        #验证成功，则写入数据库
        mh = mysqlHandler()
        student_id = mh.get_student_id()+1
        student_info = [student_id,]
        for k,value in request.form.items():
            if k == "repassword":
                continue
            student_info.append(value)
        print(student_info)
        mh.write(student_info)
        return "ok"
app.add_url_rule("/register",endpoint="register",view_func=Register.as_view(name="register"))

@app.route("/show_students")
def show_students():
    mh = mysqlHandler()
    students_info = mh.read()
    return render_template("show_students.html",students_info=students_info)





if __name__ == '__main__':
    app.config["DEBUG"] = True
    app.run()

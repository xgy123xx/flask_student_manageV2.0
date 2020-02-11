from wtforms.fields import simple,core
from wtforms import Form
from wtforms import validators

class RegisterForm(Form):
    username = simple.StringField(
        label="用户名",
        validators=[
            validators.DataRequired(message="数据不能为空"),
            validators.Length(min=4,max=16,message="大于4位小于16位")
        ],
        render_kw={"class":"form-control"}
    )
    password = simple.PasswordField(
        label="密码",
        validators = [
            validators.DataRequired(message="密码不能为空"),
            validators.Length(min=4,max=16,message="大于4位小于16位"),
            validators.Regexp(regex="\w+",message="密码必须为数字,字母，下划线")
        ],
        render_kw={"class":"form-control"}
    )

    repassword = simple.PasswordField(
        label="再次输入密码",
        validators = [
            validators.DataRequired(message="密码不能为空"),
            validators.Length(min=4,max=16,message="大于4位小于16位"),
            validators.Regexp(regex="\w+",message="密码必须为数字,字母，下划线"),
            validators.equal_to("password",message="两次密码不一致")
        ],
        render_kw={"class":"form-control"}
    )

    gender = core.RadioField(
        label="性别",
        choices=(
            (1,"男"),
            (2,"女"),
        ),
        coerce=int,
        default=1
    )
    score = core.DecimalField(
        label="年龄",
        validators = [
            # validators.length(min=0,max=3,message="小于3位")
        ]
    )




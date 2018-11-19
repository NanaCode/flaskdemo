# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/18 17:53'

from flask import Flask

app = Flask(__name__)


# @app.route('/hello/')  # hello后面加斜杆可以兼容用户输入斜杆的习惯
def hello():
    return 'Hello, Nana!!!'


app.add_url_rule('/hello', view_func=hello)  # 另一个注册路由方式
app.run(debug=True)  # 开启调试模式

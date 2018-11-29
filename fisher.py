# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/20 11:43'

from flask import Flask

app = Flask(__name__)
print(id(app))  # 核心对象初始化的app
app.config.from_object('config')

from app.web import book

if __name__ == '__main__':
    print(id(app))  # 打印最终启动的app
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])

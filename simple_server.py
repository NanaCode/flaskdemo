# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/18 17:53'

from flask import Flask, make_response

# from config import DEBUG

app = Flask(__name__)
app.config.from_object('config')  # 注意，传入的参数是模块路径，而不是文件路径
# print(app.config['DEBUG'])
# print(app.config['Debug'])  # KeyError: 'Debug'

# @app.route('/hello/')  # hello后面加斜杆可以兼容用户输入斜杆的习惯
# def hello():
#     return 'Hello, Nana!!!'

# def hello():
#     headers = {
#         # 'content-type': 'text/plain',
#         'content-type': 'application/json',
#         # 'location': 'https://www.lightthefuture.cn'
#     }
#     response = make_response('<html></html>', 404)
#     response.headers = headers
#     return response

# another way to return response
def hello():
    headers = {
        'content-type': 'application/json',
        'location': 'https://www.lightthefuture.cn'
    }
    return '<html></html>', 301, headers


app.add_url_rule('/hello', view_func=hello)  # 另一个注册路由方式

if __name__ == '__main__':
    # app.run(debug=True)  # 开启调试模式
    app.run(host='0.0.0.0', debug=True)  # 允许外网访问
    # app.run(host='0.0.0.0', port=80, debug=True)  # 修改端口
    # app.run(host='0.0.0.0', debug=DEBUG)  # 配置文件方式设置是否开启调试模式
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])  # app.config.from_object()方法访问配置文件

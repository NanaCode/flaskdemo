# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/12/1 18:10'

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # 注意，这句不能少
    return app

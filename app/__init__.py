# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/12/1 18:10'

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # 注意，别忘了这句
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)

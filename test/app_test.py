# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/12/13 22:34'

from flask import Flask, current_app

app = Flask(__name__)

a = current_app
d = current_app.config['DEBUG']

# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/20 15:45'

import requests


class HTTP:
    @staticmethod  # 静态方法
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

    # @classmethod  # 类方法
    # def get(cls, url, return_json=True):  # 但这里不需要cls
    #     r = requests.get(url)
    #     if r.status_code != 200:
    #         return {} if return_json else ''
    #     return r.json() if return_json else r.text

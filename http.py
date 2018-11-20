# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/20 15:45'

import requests


class HTTP:
    def get(self, url, return_json=True):
        r = requests.get(url)
        if r.status_code == 200:
            if return_json:
                return r.json()
            else:
                return r.text
        else:
            if return_json:
                return {}
            else:
                return ''


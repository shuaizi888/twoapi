#_*_coding:utf-8_*_

from requests import request,Session

class BaseConfig(object):
    def __init__(self,base_url='http://api.beta.acewill.net'):
        self.base_url = base_url

    def session(self):
        return Session()


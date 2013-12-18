__author__ = 'Mark Allan B. Meriales'
__email__ = 'mark.meriales@gmail.com'

import base64
from suds.client import Client
from .settings import FIVE9_API_USER_SETTINGS, FIVE9_WSDL

class Five9(object):

    @property
    def request_headers(self):
        headers = {
                'Accept-Encoding':'gzip, deflate',
                'Content-Type':'text/xml;charset=UTF-8',
                'Authorization':'Basic %s' % self.authorization,
            }
        return headers

    @property
    def authorization(self):
        return base64.b64encode('%s:%s' % (FIVE9_API_USER_SETTINGS['username'],
                                               FIVE9_API_USER_SETTINGS['password']))

    def __init__(self):
        headers = self.request_headers
        self.client = Client(FIVE9_WSDL, headers=headers)
    

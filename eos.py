from __future__ import print_function

import pyeapi
from pyeapi.eapilib import CommandError, ConnectionError

from . helpers import Result


class EAPI(object):
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

        self.conn = pyeapi.connect(host=host, username=username, password=password)

        try:
            self.conn.execute('enable')
        except ConnectionError as e:
            raise e

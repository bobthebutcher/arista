from __future__ import print_function

import pyeapi
from pyeapi.eapilib import CommandError, ConnectionError

from . helpers import Result


class EAPI(object):
    def __init__(self, host, username, password, port=443, timeout=5):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout

        self.conn = pyeapi.connect(host=host, username=username, password=password, port=port,
                                   timeout=timeout)

        try:
            self.conn.execute('enable')
        except ConnectionError as e:
            raise e

    def show_command(self, command='show version'):
        if not isinstance(command, str):
            raise TypeError('command should be a "string"')

        try:
            return self.conn.execute(['enable', command])['result'][1]
        except CommandError as e:
            raise e

    def show_commands(self, command_list=None):
        if command_list is None:
            raise TypeError('commands should be a: ["list", "of", "commands"]')

        elif isinstance(command_list, str):
            command_list = [command_list]

        commands = ['enable'] + command_list

        try:
            return self.conn.execute(commands)['result']
        except CommandError as e:
            raise e

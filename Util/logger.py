# -*- coding: utf-8 -*-

import logging

import sys


class Logger:
    """
    Logging
    """

    def __init__(self, logger=None):
        """Logging"""
        self.log = logging.getLogger(logger)
        self.log.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s:%(lineno)d %(levelname)s-->%(message)s', "%m-%d %H:%M:%S")
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.DEBUG)
        console.setFormatter(formatter)
        self.log.addHandler(console)

    def get_log(self):
        """获取log对象"""
        return self.log


if __name__ == '__main__':
    Logger()

# -*- coding: utf-8 -*-

import allure
from allure_commons.types import AttachmentType


def add_text(text, name='text'):
    """报告中添加文字"""
    allure.attach(text, name=name, attachment_type=AttachmentType.TEXT)


def add_json(json_text, name='json'):
    """报告中添加json"""
    allure.attach(json_text, name=name, attachment_type=AttachmentType.JSON)


def add_png(png, name):
    """添加图片"""
    allure.attach(png, name=name, attachment_type=AttachmentType.PNG)

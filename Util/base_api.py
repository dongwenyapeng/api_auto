
import os

import allure
import pytest
import requests
from loguru import logger

from Config.configapi import get_machine_env
from Util.handle_assert import HandleAssert
from Util.handle_path import CONF_DIR
from Util.utils import Utils


class BaseApi:

    if get_machine_env() == 'test':
        conf_path = os.path.join(CONF_DIR, 'configapi.yaml')
    elif get_machine_env() == 'pre':
        conf_path = os.path.join(CONF_DIR, 'configapi_pre.yaml')
    else:
        conf_path = os.path.join(CONF_DIR, 'configapi_prod.yaml')

    # 配置文件数据
    conf_data = Utils().handle_yaml(conf_path)
    hostikapp = conf_data['env']['hostikapp']
    hostikapp_search_headers =conf_data['request_headers']['ikapp-search-headers']





    def send_http(self, data: dict):
        """
        发送http请求
        :param data: 请求数据
        :return:
        """
        try:
            # print(" the search headers is ",BaseApi.searchheaders)
            self.__api_log(**data)
            response = requests.request(**data)
            print(" the response >>> ",response)
            logger.info(f"响应结果为：{response.status_code}")
        except Exception as e:
            logger.error(f'发送请求失败，请求参数为：{data}')
            logger.exception(f'发生的错误为：{e}')
            raise e
        else:
            return response

    @staticmethod
    def get_yaml(file_name):
        """
        读取yaml文件
        :param file_name: 文件路径名称
        :return: dict
        """
        return Utils.handle_yaml(file_name)

    @staticmethod
    def get_token(response):
        """
        处理并提取token
        :param response:
        :return:
        """
        return Utils.handle_token(response)

    @staticmethod
    @allure.step('step:数据替换')
    def template(source_data: str, data: dict):
        """
        替换数据
        :param source_data: 源数据
        :param data: 替换内容，如{data:new_data}
        :return:
        """

        return Utils.handle_template(source_data, data)

    @staticmethod
    def to_two_decimal(data):
        """
        将整数或浮点数转化为两位数decimal
        :param data:
        :return:
        """
        return Utils.handle_decimal(data)

    @staticmethod
    def random_phone():
        """
        生成随机手机号
        :return:
        """
        return Utils.handle_random_phone()

    @staticmethod
    def __api_log(method, url, headers=None, params=None, json=None):
        logger.info(f"请求方式：{method}")
        logger.info(f"请求地址：{url}")
        logger.info(f"请求头：{headers}")
        logger.info(f"请求参数：{params}")
        logger.info(f"请求体：{json}")

    @staticmethod
    def assert_equal(ex, re):
        """
        断言相等
        :param ex:预期结果
        :param re:实际结果
        :return:
        """
        return HandleAssert.eq(ex, re)

    @staticmethod
    def assert_contains(content, target):
        """
        断言包含
        :param content: 文本内容
        :param target: 目标文本
        :return:
        """
        return HandleAssert.contains(content, target)


if __name__ == '__main__':
    a = BaseApi()
    a.template()


from decimal import Decimal
from string import Template
from faker import Faker

import yaml
#from jsonpath import jsonpath
from loguru import logger


class Utils:
    @classmethod
    def handle_yaml(cls, file_name):
        """
        读取yaml文件
        :param file_name:
        :return:
        """
        try:
            yaml_data = yaml.safe_load(open(file_name, encoding='utf-8'))
        except Exception as e:
            logger.error(f'yaml文件读取失败，文件名称：{file_name}')
            raise e
        else:
            return yaml_data

    @classmethod
    def handle_token(cls, response):
        """
        组装token
        :param response:
        :return:
        """
        # token_type = jsonpath(response.json(), '$..token_type')[0]
        # token_value = jsonpath(response.json(), '$..token')[0]
        # token = f'{token_type} {token_value}'
        token = '123456'
        return token

    @classmethod
    def handle_template(cls, source_data, replace_data: dict, ):
        """
        替换文本变量
        :param source_data:
        :param replace_data:
        :return:
        """
        res = Template(str(source_data)).safe_substitute(**replace_data)
        return yaml.safe_load(res)

    @classmethod
    def handle_decimal(cls, data: int):
        """
        将小数或整数转换为两位数decimal
        :param data:
        :return:
        """
        x = '{0:.2f}'.format(float(data))
        return Decimal(x)

    @classmethod
    def handle_random_phone(cls):
        """
        生成随机手机号
        :return:
        """
        fake = Faker(locale='zh_CN')
        phone_number = fake.phone_number()
        return phone_number


if __name__ == '__main__':
    a = Utils.handle_random_phone()
    print(a)

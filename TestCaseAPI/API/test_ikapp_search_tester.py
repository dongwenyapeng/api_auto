# -*- coding:utf-8 -*-

__author__ = "dongyunpeng"

import json
import os
import re

import allure
import pytest
import requests
import yaml

from API.api_search.search_api import SearchApi
from Config.configapi import get_machine_env
from Util.base_api import BaseApi
from Util.handle_path import DATA_DIR


if get_machine_env() == 'test':
    case_data_path = os.path.join(DATA_DIR, 'search_api.yaml')
    print("teetettette",case_data_path)
elif get_machine_env() == 'pre':
    case_data_path = os.path.join(DATA_DIR, 'epsearch_entrance_all_pre_data.yaml')
else:
    case_data_path = os.path.join(DATA_DIR, 'epsearch_entrance_all_pro_data.yaml')

datas = yaml.safe_load(open(case_data_path, encoding='utf-8'))

@pytest.mark.ikappsearsh
@allure.feature('测试-ikapp搜索项目-APITesting')
class TestRequestIkappSearch(SearchApi):
    url = BaseApi().hostikapp
    session = requests.session()
    @allure.story('ikapp-search')
    @allure.title('ikapp-search-testcase001')
    @allure.description('全部简单验证demo')
    @allure.testcase("https://www.baidu.com", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.parametrize('data', datas['ikapp_search_api'])
    def test_search_all_posts(self, data):
        print("======data['json']  ========",type(data['json']) ,data['json'])
        print("======data['uri']  ========",type(data['uri']), data['uri'])
        result = self.ikapp_search_api(data['uri'], data['json']).json()


        # # 断言状态码及返回类型
        assert result['code'] == 1
        for key_results, value_results in result.items():
            if key_results == "results":
                assert value_results
                for i in value_results:
                    for key_type,value_type in i.items():
                        if key_type == "searchResultType":
                            assert value_type == 1
                        pass
            pass



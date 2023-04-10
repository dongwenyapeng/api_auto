
import pytest
from Util.base_api import BaseApi
from Util.wrapper import api_call


@pytest.mark.api
class SearchApi(BaseApi):

    #ikappsearch接口
    @api_call
    def ikapp_search_api(self, httpuri, jsonentity):
        # with allure.step('请求地址'):
        #     allure.attach('{}'.format(self.hostikapp + httpuri), name='post请求')
        # with allure.step('请求header'):
        #     allure.attach('{}'.format(self.hostikapp_search_headers), name='请求header')

        data = {
            'url': self.hostikapp + httpuri,
            'method': 'post',
            'headers': self.hostikapp_search_headers,
            'json': jsonentity,
        }
        response = self.send_http(data)
        return response






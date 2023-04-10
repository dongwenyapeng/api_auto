import os
from string import Template
import yaml

from API.api_search.search_api import SearchApi
from Util.base_api import BaseApi
from Util.handle_mysql import HandleMysql
from Util.handle_path import DATA_DIR, CONF_DIR
from Util.time_conversion import TimeConversion


class BuildSearchActivity(SearchApi):
#每次创建活动前先把 已有的活动都失效，再重新创建活动
    p = os.path.join(CONF_DIR, 'configapi.yaml')
    a = BaseApi()
    conf = a.get_yaml(p)
    mysql = conf['mysql_activity']
    db = HandleMysql(**mysql)
    result_id = db.get_all('SELECT id FROM discover.activity WHERE status=0')
    print(type(result_id), result_id)
    num = 0
    for num in result_id:
        for num in num:
            print(num, type(num))
            sql = "update discover.activity set status = 2 where id ='{}'".format(num)
            db.update(sql)

    def search_activity_new_build(self):
        case_data_path = os.path.join(DATA_DIR, 'activity_data.yaml')
        end_time = TimeConversion().date_now_one()
        state_time = TimeConversion().date_now()
        with open(case_data_path, encoding='utf-8')as fp:
            inversion = Template(fp.read())
            yaml_time_conversion = inversion.safe_substitute({'tomorrow_time': end_time, 'current_time': state_time})
            datas = yaml.safe_load(yaml_time_conversion)
            for data in datas['ep_build_activity_new']:
                print(
                    "读取yaml文件", type(data), data
                )
        result = self.search_build_activity_api(data['uri'], data['json']).json()
        print("===response===", result, type(result))
        return result


# a = BuildSearchActivity().search_activity_new_build()

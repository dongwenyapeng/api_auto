
import os

import pytest
from loguru import logger


@pytest.mark.api
# logger.add('./log/{time}.log', rotation='20 MB', retention='1 week', encoding='utf-8')
# pytest.main(['-s', r"--alluredir=report/json", "--clean-alluredir"])
# os.system('allure generate ./report/json -o ./report/html -c')
# # pytest.main(['-s'])
def main():
    logger.add('./API/logapi/{time}.log', rotation='20 MB', retention='1 week', encoding='utf-8')
    pytest.main(['-s','./TestCaseAPI','-m','searchentrace',r"--alluredir=./API/report/json", "--clean-alluredir"])
    os.system('allure generate ./API/report/json -o ./API/report/html -c')
    print('This message is ep-ip department api testing done')


if __name__ == '__main__':
    main()

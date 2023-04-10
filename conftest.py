
import pytest
from loguru import logger

from Util.handle_mysql import HandleMysql



@pytest.fixture(scope='class')
def connect_mysql(request):
    """连接数据库"""
    db = HandleMysql(**request.param)
    yield db
    db.close()


@pytest.fixture(scope='session', autouse=True)
def task_mark():
    logger.debug("{:=^50}".format('测试任务开始'))
    yield
    logger.debug("{:=^50}".format('测试任务结束'))


@pytest.fixture(autouse=True)
def case_mark():
    logger.debug("{:=^50}".format('用例开始'))
    yield
    logger.debug("{:=^50}".format('用例结束'))

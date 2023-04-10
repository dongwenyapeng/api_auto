

# 项目目录的路径 | 如果运行的时候项目目录路径出错，使用上面abspath的方式来获取当前文件的绝对路径
import os

BASEDIR = os.path.dirname(os.path.dirname(__file__))
print(BASEDIR)
# 配置文件的路径
CONF_DIR = os.path.join(BASEDIR, "Config")
CONFIG_DIR = os.path.join(CONF_DIR, 'configapi.yaml')
print(CONFIG_DIR)
# 用例数据的目录
DATA_DIR = os.path.join(BASEDIR, "API/data")
print(DATA_DIR)
# 日志文件目录
LOG_DIR = os.path.join(BASEDIR, "API/log")
# 测试报告的路
REPORT_DIR = os.path.join(BASEDIR, "API/reports")
# 测试用例模块所在的目录
CASE_DIR = os.path.join(BASEDIR, "TestCases/API")
print(CASE_DIR)

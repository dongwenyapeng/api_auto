import os

CONF_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/Config/"

def get_machine_env():
    """获取环境"""
    with open(f'{CONF_PATH}/envmachine.ini', encoding='utf-8') as file:
        env = file.read()
        print("test",env)
    return env

a = get_machine_env()
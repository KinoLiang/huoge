# -*- coding:utf-8 -*-
# 配置文件

import pytest
from optparse import OptionParser

# 注册自定义参数
def pytest_addoption(parser):
    parser.addoption("--env", action="store",
                     default='test',
                     choices=['dev', 'test', 'st'],
                     help="将自定义命令行参数 ’--env' 添加到 pytest 配置中")
    args = ["-f", "foo.txt"]


# 获取配置参数的值
@pytest.fixture(scope='session')
def env(pytestconfig):
    print(pytestconfig.getoption('--env'))
    return pytestconfig.getoption('--env')

# 将自定义参数的值打印出来
@pytest.fixture(autouse=True)
def fix_1(env):
    print('\n --env的值：', env)

parser = OptionParser()

if __name__ == '__main__':
    # 使用参数
    parser.add_option("-f", "--file",
                      action="store", type="string", dest="filename")
    args = ["-f", "foo.txt"]
    (options, args) = parser.parse_args(args)
    print(options.filename)

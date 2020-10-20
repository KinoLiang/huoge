# -*- coding:utf-8 -*-
# @time   :2020/10/19 16:41
# @Author   :Kino

import pytest,os
from pythoncode.calculator import Calculator

@pytest.fixture(scope='module', autouse=True)
def get_calc():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")

# 添加命令行参数
def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     # default: 默认值，命令行没有指定host时，默认用该参数值
                     default="test",
                     choices=['dev', 'test', 'st'],
                     help="test case project host address")

# autouse=True自动执行该前置操作
@pytest.fixture(scope="session", autouse=True)
def host(request):
    '''获取命令行参数'''
    # 获取命令行参数给到环境变量
    os.environ["host"] = request.config.getoption("--env")
    print("当前用例运行测试环境:%s"%os.environ["host"])


if __name__ == '__main__':
    pytest.main(['-s','--env'])


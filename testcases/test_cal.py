# -*- coding:utf-8 -*-
# @time   :2020/10/16 14:57
# @Author   :Kino

import pytest

from pythoncode.calculator import Calculator

class TestCal:

    # 初始化计算器
    cal = Calculator()

    def setup(self):
        # 用例执行前初始化
        print('计算开始')

    def teardown(self):
        # 用例执行结束
        print('计算结束')

    def setup_class(self):
        # 测试类执行初始化
        print('开始执行用例')

    def teardown_class(self):
        # 测试类执行完毕
        print('用例执行结束')

    # 加法用例设计
    @pytest.mark.parametrize('a,b,expect',[
        [8,3,11],[185221,98545121254111111,98545121254296332],[23.1332,0.8521,23.9853],[-15,-1.62,-16.62],[1,0,1]
    ],ids=['int_case','big_case','fload_case','minus_case','zero_case'])
    def test_add(self, a, b, expect):
        result = self.cal.add(a, b)
        assert result==expect

    # 减法用例设计
    @pytest.mark.parametrize('a,b,expect',[
        [82,15,67],[85000,7800,77200],[80.54,150.54,-70.0],[12,-8.5,20.5],[1,0,1]
    ],ids=['int_case','big_case','fload_case','minus_case','zero_case'])
    def test_sub(self, a, b, expect):
        result = self.cal.sub(a, b)
        assert result==expect

    # 乘法用例设计
    @pytest.mark.parametrize('a,b,expect',[
        [6,9,54],[500,240,120000],[2.6,3.4,8.84],[-15,2.4,-36.0],[18,0,0]
    ],ids=['int_case','big_case','fload_case','minus_case','zero_case'])
    def test_mul(self, a, b, expect):
        result = self.cal.mul(a, b)
        assert result==expect

    # 除法用例设计
    @pytest.mark.parametrize('a,b,expect',[
        [54,6,9],[120000,500,240],[340,3.4,100],[15,-1.5,-10],[1,0,1]
    ],ids=['int_case','big_case','fload_case','minus_case','zero_case'])
    def test_div(self, a, b, expect):
        result = self.cal.div(a, b)
        assert result==expect


if __name__ == '__main__':
    pytest.main()

# -*- coding:utf-8 -*-
# @time   :2020/10/16 14:57
# @Author   :Kino
import os
import time
import pytest, allure

from config.config import proDir

from pythoncode.calculator import Calculator

class TestCal:
    #使用fixture环境初始化



    # 加法用例设计
    @allure.title('加法用例')
    @pytest.mark.smoketest
    @pytest.mark.run(order=1)   # 添加运行顺序
    @pytest.mark.parametrize('a,b,expect',[
        [8,3,11],[185221,98545121254111111,98545121254296332],[23.1332,0.8521,23.9853],[-15,-1.62,-16.62],[1,0,1]
    ],ids=['int_case','big_case','fload_case','minus_case','zero_case'])
    def test_add(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert result==expect

    # 减法用例设计
    @allure.title('减法用例')
    @pytest.mark.smoketest
    @pytest.mark.run(order=2)  # 添加运行顺序
    @pytest.mark.parametrize('a,b,expect',[
        [82,15,67],[85000,7800,77200],[80.54,150.54,-70.0],[12,-8.5,20.5],[1,0,1]
    ],ids=['int_case','big_case','fload_case','minus_case','zero_case'])
    def test_sub(self, get_calc, a, b, expect):
        result = get_calc.sub(a, b)
        assert round(result, 3)==expect

    # 乘法用例设计
    @allure.title('乘法用例')
    @pytest.mark.systemtest
    @pytest.mark.run(order=3)  # 添加运行顺序
    @pytest.mark.parametrize('a,b,expect',[
        [6,9,54],[500,240,120000],[2.6,3.4,8.84],[-15,2.4,-36.0],[18,0,0]
    ],ids=['int_case','big_case','fload_case','minus_case','zero_case'])
    def test_mul(self,get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        assert result==expect

    # 除法用例设计
    @allure.title('除法用例')
    @pytest.mark.run(order=4)  # 添加运行顺序
    @pytest.mark.smoketest
    @pytest.mark.parametrize('a,b,expect',[
        [54,6,9],[120000,500,240],[340,3.4,100],[15,-1.5,-10]
    ],ids=['int_case','big_case','fload_case','minus_case'])
    def test_div(self, get_calc, a, b, expect):
        result = get_calc.div(a, b)
        assert result==expect

    # 除法异常场景
    @allure.title('除法异常场景用例')
    @pytest.mark.run(order=4)  # 添加运行顺序
    @pytest.mark.hogwards
    @pytest.mark.parametrize('a,b', [[1, 0]], ids=['error_case'])
    def test_div(self, get_calc, a, b):
        with pytest.raises(ZeroDivisionError):
            print('数据报错')
            get_calc.div(a, b)

if __name__ == '__main__':
    # 生成allure报告
    xml_path = os.path.join(proDir,r'report\xml')
    html_path = os.path.join(proDir,r'report\html')
    #添加'--clean-alluredir'则可去除历史报告数据
    pytest.main(['-s', '-v', 'test_cal.py', '-m systemtest', '--alluredir', xml_path])
    time.sleep(1)
    #os.system(r'allure generate {0} -o {1} --clean'.format(xml_path, html_path))
    #os.system(r'allure open {}'.format(html_path))

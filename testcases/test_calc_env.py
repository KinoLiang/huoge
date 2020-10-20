# -*- coding:utf-8 -*-
# @time   :2020/10/16 14:57
# @Author   :Kino

import pytest
import yaml
import os


# 解析测试数据
def get_test_data(env):
    print(os.environ[env])
    if env == 'test':
        data_file = './datas/calc_env_test.yml'
    elif env == 'dev':
        data_file = './datas/calc_env_dev.yml'
    elif env == 'st':
        data_file = './datas/calc_env.yml'
    else:
        data_file = './datas/calc.yml'
    with open(data_file, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        add_datas = datas['calc']['add']['data']
        add_ids = datas['calc']['add']['ids']
    return [add_datas, add_ids]


class TestCalc:
    # @pytest.mark.hogwarts
    # @pytest.mark.parametrize('a,b,expect', get_test_data(os.environ['host'])[0], ids=get_test_data(os.environ['host'])[1])
    # def test_add(self, get_calc, host, a, b, expect):
    #     result = get_calc.add(a, b)
    #     assert result == expect

    @pytest.mark.hogwards
    def test_add_env(self, get_calc, host):
        if os.environ['host'] == 'test':
            data_file = '../datas/calc_test.yml'
        elif os.environ['host'] == 'dev':
            data_file = '../datas/calc_dev.yml'
        elif os.environ['host'] == 'st':
            data_file = '../datas/calc_st.yml'
        else:
            data_file = '../datas/calc.yml'
        with open(data_file, encoding='utf-8') as f:
            datas = yaml.safe_load(f)
            add_datas = datas['calc']['add']['datas']
        for data in add_datas:
            result = get_calc.add(data[0], data[1])
            print('计算过程：{0} + {1} ？ {2}'.format(data[0], data[1], result))
            assert result == data[2]

# if __name__ == '__main__':
#     pytest.main(['-v', '-s', 'test_calc_env.py', '--env=dev'])

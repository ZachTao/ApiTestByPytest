# -*- coding = utf-8 -*
# 运行所有用例，并生成allure报告
import os
import pytest
import time


if __name__ == '__main__':
    pytest.main()
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    report_path = r"F:/PycharmProjects/ApiTestByPytest/reports/" + now + '_report'
    if not os.path.exists(report_path):
        os.makedirs(report_path)
    os.system(f"allure generate ./temp -o {report_path} --clean")




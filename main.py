# -*- coding = utf-8 -*
# 运行所有用例，并生成allure报告
import os
import pytest


if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./temp -o ./reports --clean")


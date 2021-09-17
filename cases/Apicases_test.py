import allure
from RequestGo import ReqGo
from ReadYml import ReadYml
import pytest
from common.AssertImp import AssertImp

@allure.feature("Api接口测试")
class TestCases:

    def set_up(self):
        print('测试开始')

    @allure.story("电话归属地查询")
    @pytest.mark.parametrize('data', ReadYml().get_mobilocal_data())
    def test_phonelocation(self, data):
        '''电话归属地查询'''
        method = data[0]
        url = data[1]
        param = data[2]
        assertdata = data[3]
        with allure.step("发送Api接口请求"):
            respon = ReqGo().req_go(method, url, param)
            AssertImp.assert_response(self, respon.json(), assertdata)


    @allure.story("驾考宝典查询")
    @pytest.mark.parametrize('data', ReadYml().get_drivquesbank_data())
    def test_driquesbank(self, data):
        '''驾考宝典查询'''
        method = data[0]
        url = data[1]
        param = data[2]
        assertdata = data[3]
        with allure.step("发送Api接口请求"):
            respon = ReqGo().req_go(method, url, param)
            AssertImp.assert_response(self, respon, assertdata)

    @allure.story("星座运势查询")
    @pytest.mark.parametrize('data', ReadYml().get_starluck_data())
    def test_starluck(self, data):
        '''运势查询'''
        method = data[0]
        url = data[1]
        param = data[2]
        assertdata = data[3]
        with allure.step("发送Api接口请求"):
            respon = ReqGo().req_go(method, url, param)
            AssertImp.assert_response(self, respon.json(), assertdata)

    @allure.story("疫情防控查询")
    @pytest.mark.parametrize('data', ReadYml().get_defenceyq_data())
    def test_defenceyq(self, data):
        '''疫情防控查询'''
        method = data[0]
        url = data[1]
        param = data[2]
        assertdata = data[3]
        with allure.step("发送Api接口请求"):
            respon = ReqGo().req_go(method, url, param)
            AssertImp.assert_response(self, respon.json(), assertdata)

    def teardown(self):
        print('测试结束')


if __name__ == '__main__':
    A = TestCases()
    A.test_driquesbank(ReadYml().get_mobilocal_data())
    # pytest.main()

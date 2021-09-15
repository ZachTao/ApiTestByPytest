from RequestGo import ReqGo
from ReadYml import ReadYml
import pytest


class Test_Cases:

    @pytest.mark.parametrize('data', ReadYml().get_testcase_data('testcase.yml'))
    def test_phonelocation(self, data):
        method = data['Mobilelocationquery']['method']
        url = data['Mobilelocationquery']['url']
        params = data['Mobilelocationquery']['params']
        ReqGo().req_go(method, url, params)


if __name__ == '__main__':
    A = Test_Cases()
    A.test_phonelocation(ReadYml().get_testcase_data('testcase.yml'))

import json

from RequestGo import ReqGo
from ReadYml import ReadYml
import pytest


class Test_Cases:

    @pytest.mark.parametrize('data', ReadYml().get_mobilocal_data())
    def test_phonelocation(self, data):
        method = data[0]
        url =data[1]
        param = data[2]
        ReqGo().req_go(method, url, param)

    @pytest.mark.parametrize('data', ReadYml().get_drivquesbank_data())
    def test_driquesbank(self, data):
        method = data[0]
        url = data[1]
        param = data[2]
        ReqGo().req_go(method, url, param)

    @pytest.mark.parametrize('data', ReadYml().get_starluck_data())
    def test_starluck(self, data):
        method = data[0]
        url = data[1]
        param = data[2]
        ReqGo().req_go(method, url, param)

    @pytest.mark.parametrize('data', ReadYml().get_defenceyq_data())
    def test_defenceyq(self, data):
        method = data[0]
        url = data[1]
        param = data[2]
        ReqGo().req_go(method, url, param)


if __name__ == '__main__':
    # A = Test_Cases()
    # A.test_phonelocation(ReadYml().get_mobilocal_data())
    pytest.main()

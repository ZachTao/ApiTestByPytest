import jsonpath


class AssertImp:

    def assert_response(self, response, validate):
        for val in validate:
            for keynames in val:
                key_name = keynames
                expect_result = val[key_name]
            actual_result = jsonpath.jsonpath(response, key_name)
            print("实际结果：%s" % actual_result[0])
            print("期望结果：%s" % expect_result)
            assert actual_result[0] == expect_result


if __name__ == '__main__':
    AssertImp.assert_response()

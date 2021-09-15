import requests


class ReqGo:
    session = requests.session()  # 同一个会话

    def req_go(self, method, url, params, **kwargs):  # kwargs可以用于上传文件 file=
        method = str(method).lower()
        try:
            if method == 'post':
                bak_result = ReqGo.session.request('post', url, params)
                return bak_result.json()
            elif method == 'get':
                bak_result = ReqGo.session.request('get', url, params)
                return bak_result
            elif method == 'put':
                bak_result = ReqGo.session.request('put', url, params)
                return bak_result
            elif method == 'delete':
                bak_result = ReqGo.session.request('delete', url, params)
                return bak_result
            else:
                print('请检查method列数据')
        except Exception as e:
            print('发送请求异常:' + e)

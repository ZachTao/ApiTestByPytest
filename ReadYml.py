# -*- coding=utf-8 -*-
import os
import yaml


class ReadYml:

    def read_standard(self, yml_name):
        with open(os.getcwd() + "/CaseByYml/"+yml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value

    def clear_yaml(self):
        with open(os.getcwd()+"/CaseByYml"+'testcase.yml', mode='w', encoding='utf-8') as f:
            f.truncate()

    def get_mobilocal_data(self):
        methods = []
        urls = []
        paramss = []
        curpath = os.path.dirname(os.path.realpath(__file__))  # 获取文件目录
        cfgpath = os.path.join(curpath, 'CaseByYml/testcase.yml')
        with open(cfgpath, mode='r', encoding='utf-8') as f:
            datas = yaml.load(f, yaml.FullLoader)
            f.close()
            for data in datas:
                a = list(data.keys())
                if a[0] == 'Mobilelocationquery':
                    mel0 = data['Mobilelocationquery']['method']
                    methods.append(mel0)
                    mel1 = data['Mobilelocationquery']['url']
                    urls.append(mel1)
                    mel2 = data['Mobilelocationquery']['params']
                    paramss.append(mel2)
                    list_param = list(zip(methods, urls, paramss))
                    return list_param

    def get_drivquesbank_data(self):
        methods = []
        urls = []
        paramss = []
        curpath = os.path.dirname(os.path.realpath(__file__))  # 获取文件目录
        cfgpath = os.path.join(curpath, 'CaseByYml/testcase.yml')
        with open(cfgpath, mode='r', encoding='utf-8') as f:
        # with open(os.getcwd()+'/CaseByYml/'+'testcase.yml', mode='r', encoding='utf-8') as f:
            datas = yaml.load(f, yaml.FullLoader)
            f.close()
            for data in datas:
                a = list(data.keys())
                if a[0] == 'DriverQuestionBank':
                    mel0 = data['DriverQuestionBank']['method']
                    methods.append(mel0)
                    mel1 = data['DriverQuestionBank']['url']
                    urls.append(mel1)
                    mel2 = data['DriverQuestionBank']['params']
                    paramss.append(mel2)
                    list_param = list(zip(methods, urls, paramss))
                    return list_param

    def get_starluck_data(self):
        methods = []
        urls = []
        paramss = []
        curpath = os.path.dirname(os.path.realpath(__file__))  # 获取文件目录
        cfgpath = os.path.join(curpath, 'CaseByYml/testcase.yml')
        with open(cfgpath, mode='r', encoding='utf-8') as f:
        # with open(os.getcwd() + '/CaseByYml/' + 'testcase.yml', mode='r', encoding='utf-8') as f:
            datas = yaml.load(f, yaml.FullLoader)
            f.close()
            for data in datas:
                a = list(data.keys())
                if a[0] == 'Starluck':
                    mel0 = data['Starluck']['method']
                    methods.append(mel0)
                    mel1 = data['Starluck']['url']
                    urls.append(mel1)
                    mel2 = data['Starluck']['params']
                    paramss.append(mel2)
                    list_param = list(zip(methods, urls, paramss))
                    return list_param

    def get_defenceyq_data(self):
        methods = []
        urls = []
        paramss = []
        curpath = os.path.dirname(os.path.realpath(__file__))  # 获取文件目录
        cfgpath = os.path.join(curpath, 'CaseByYml/testcase.yml')
        with open(cfgpath, mode='r', encoding='utf-8') as f:
        # with open(os.getcwd() + '/CaseByYml/' + 'testcase.yml', mode='r', encoding='utf-8') as f:
            datas = yaml.load(f, yaml.FullLoader)
            f.close()
            for data in datas:
                a = list(data.keys())
                if a[0] == 'DefenceYQ':
                    mel0 = data['DefenceYQ']['method']
                    methods.append(mel0)
                    mel1 = data['DefenceYQ']['url']
                    urls.append(mel1)
                    mel2 = data['DefenceYQ']['params']
                    paramss.append(mel2)
                    list_param = list(zip(methods, urls, paramss))
                    return list_param


if __name__ == '__main__':
    A = ReadYml()
    A.get_mobilocal_data()


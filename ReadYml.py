# -*- coding=utf-8 -*-
import os
import yaml
import xlrd


class ReadYml:

    def read_standard(self, yml_name):
        with open(os.getcwd() + "/CaseByYml/"+yml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value

    def clear_yaml(self):
        with open(os.getcwd()+"/CaseByYml"+'testcase.yml', mode='w', encoding='utf-8') as f:
            f.truncate()

    def get_testcase_data(self, yml_name):
        with open(os.getcwd()+'/CaseByYml/'+yml_name, mode='r', encoding='utf-8') as f:
            data = yaml.load(f, yaml.FullLoader)
            f.close()
            return data


if __name__ == '__main__':
    A = ReadYml()
    A.get_mobile_location_data('testcase.yml')


# -*- coding=utf-8 -*-
import os
import yaml


class ReadYml:

    def read_standard(self, yml_name):
        with open(os.getcwd() + "/CaseByYml/"+yml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value

    def clear_yaml(self):
        with open(os.getcwd()+"/CaseByYml"+'1.yml', mode='w', encoding='utf-8') as f:
            f.truncate()


if __name__ == '__main__':
    A = ReadYml()
    A.read_standard('Standard.yml')


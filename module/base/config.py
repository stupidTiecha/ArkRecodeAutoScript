import os
from module.base.const import BaseConst
import json


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@Singleton
class Config(object):
    config = {}

    def __init__(self):
        self.__load_config()

    def __load_config(self):
        for _ in os.listdir(BaseConst.CONFIG_PATH):
            if _.endswith('.json'):
                keyword = _[0:-5]
                with open(BaseConst.CONFIG_PATH + _.__str__()) as f:
                    con = f.read()
                    self.config.__setitem__(keyword, json.loads(con))

    def get_config(self, section, key):
        return self.config.get(section).get(key)


if __name__ == '__main__':
    config = Config()
    cfg1 = config.get_config("config", "Emulator_Serial")
    print(cfg1)

import uiautomator2 as u2
from module.base.config import Config
from module.base.logger import logger


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@Singleton
class DeviceManager:
    devices = {}

    def __init__(self):
        cfg = Config()
        serials = cfg.get_config("config", "Emulator_Serial")
        serials = serials.split(",")
        for _ in range(serials.__len__()):
            self.devices.__setitem__(serials[_], u2.connect(serials[_]))
        logger.debug("Device Manager init complete")


def get_device(serial):
    return DeviceManager().devices[serial]


if __name__ == "__main__":
    # pass
    device_manager = DeviceManager()
    device_manager2 = DeviceManager()
    device_manager3 = DeviceManager()

    # ds = device_manager.devices
    # print(device_manager.devices)

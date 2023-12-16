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
            self.devices.__setitem__(serials[_], u2.connect_usb(serials[_]))
        logger.debug("Device Manager init complete")


def get_device(serial):
    return DeviceManager().devices[serial]


def refresh_device(serial):
    dm = DeviceManager()
    _d = u2.connect_usb(serial)
    dm.devices[serial] = _d
    return _d


if __name__ == "__main__":
    d = u2.connect_usb("emulator-5554")
    print(d.info)
    # "emulator-5554""emulator-5554"
    # pass
    # device_manager = DeviceManager()
    # device_manager2 = DeviceManager()
    # device_manager3 = DeviceManager()

    # ds = device_manager.devices
    # print(device_manager.devices)

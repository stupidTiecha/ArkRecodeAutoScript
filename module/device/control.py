"""
应用控制，检查是否存在应用，启动，重启应用。。。
"""

import uiautomator2 as u2
from module.base.const import BaseConst
from adbutils import adb
from uiautomator2 import Device


def check_app_exist(device: Device) -> bool:
    if device.app_list(BaseConst.APP_NAME):
        return True
    return False


class AppControl:

    def __init__(self):
        self.package_name = BaseConst.APP_NAME

    def app_is_running(self, device: Device) -> bool:
        package_name = device.app_current()
        return package_name.get("package") == BaseConst.APP_NAME



if __name__ == '__main__':
    app = AppControl()
    d = u2.connect_usb("emulator-5554")
    print(check_app_exist(d))
    print(app.app_is_running(d))

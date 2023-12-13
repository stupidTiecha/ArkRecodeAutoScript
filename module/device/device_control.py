"""
应用控制，检查是否存在应用，启动，重启应用。。。
"""
import time

import cv2
import numpy as np
from uiautomator2 import Device
from PIL import Image

import module.device.device_manager as dm
from module.base.const import BaseConst
from module.base.logger import logger


class DeviceControl:
    device: Device = None

    def __init__(self, serial):
        self.device = dm.get_device(serial=serial)

    def app_is_running(self) -> bool:
        package_name = self.device.app_current()
        return package_name.get("package") == BaseConst.APP_NAME

    def check_app_exist(self) -> bool:
        if self.device.app_list(BaseConst.APP_NAME):
            return True
        return False

    def app_start(self):
        self.device.app_start(BaseConst.APP_NAME)

    def app_stop(self):
        self.device.app_stop(BaseConst.APP_NAME)

    def screen_shot(self):
        image = self.device.screenshot(format='raw')
        image = np.frombuffer(image, np.uint8)
        if image is None:
            raise ImageTruncated('Empty image after reading from buffer')

        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        if image is None:
            raise ImageTruncated('Empty image after cv2.imdecode')

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if image is None:
            raise ImageTruncated('Empty image after cv2.cvtColor')

        return image


class ImageTruncated(Exception):
    pass


if __name__ == '__main__':
    start = time.time()
    appControl = DeviceControl("emulator-5554")
    end = time.time()
    logger.info(f'连接uiautomator耗时{str(end - start)}')

    time.sleep(0.1)
    start = time.time()
    # img = appControl.device.screenshot()
    img2 = appControl.screen_shot()
    img = Image.fromarray(img2.astype('uint8'))
    img.show("222")
    end = time.time()
    print(f'截图耗时{str(end - start)}')
    appControl2 = DeviceControl("emulator-5554")



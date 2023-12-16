"""
应用控制，检查是否存在应用，启动，重启应用。。。
"""
import os
import time

import cv2
import numpy as np
from uiautomator2 import Device
from adbutils import adb, AdbDevice
from PIL import Image

import module.device.device_manager as dm
from module.base.const import BaseConst
from module.base.logger import logger


class DeviceControl:
    device: Device = None
    serial = None

    def __init__(self, serial):
        self.device = dm.get_device(serial=serial)
        self.serial = serial

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

    def click(self, pos: tuple[int, int]):
        x, y = pos
        self.device.click(x, y)

    def long_click(self, pos: tuple[int, int], duration: float = 0.5):
        x, y = pos
        self.device.long_click(x, y, duration)

    def swipe(self, fp: tuple[int, int], tp: tuple[int, int], duration=None, steps=None):
        fx, fy = fp
        tx, ty = tp
        self.device.swipe(fx, fy, tx, ty, duration, steps)

    def refresh(self):
        self.device = dm.refresh_device(self.serial)
        return self.device


class ImageTruncated(Exception):
    pass


if __name__ == '__main__':
    start = time.time()
    # todo 需要等待设备连接
    os.chdir('../../bin/adb')
    logger.debug(f'current dir: {os.getcwd()}')
    while 1:
        r1 = os.popen('adb -s emulator-5554 shell ps | find "uiautomator"')
        var1 = r1.read()
        if var1 == '':
            target_app = 'com.github.uiautomator'
            r2 = os.popen('adb -s emulator-5554 shell pm list packages -3')
            var2 = r2.read()
            count = var2.count(target_app)
            if count is not 2:
                logger.error(f'uiautomator packages not full installed: need 2 but found {count} packages')
                break
            logger.debug(f'init app: {target_app}')
            os.system('adb -s emulator-5554 shell  /data/local/tmp/atx-agent server -d')
        else:
            logger.debug(f'uiautomator init completed at : {var1}')
            time.sleep(2)
            break
        time.sleep(3)

        # d.shell(cmdargs=[' /data/local/tmp/atx-agent server -d'])
    # r2 = d.shell(
    #     ' am instrument -w -r -e debug false -e class com.github.uiautomator.stub.Stub com.github.uiautomator.test/androidx.test.runner.AndroidJUnitRunner',
    #     timeout=20)
    # d.app_uninstall('com.github.uiautomator')

    appControl = DeviceControl("emulator-5554")
    d = appControl.device
    print(d.info)
    # appControl.click((540, 190))
    appControl.long_click((540, 190), 5.0)
    # appControl.swipe((150, 444), (835, 423), steps=1)
    end = time.time()
    logger.info(f'连接uiautomator耗时{str(end - start)}')
    time.sleep(5)

    time.sleep(0.1)
    # start = time.time()
    # img = appControl.device.screenshot()
    # img2 = appControl.screen_shot()
    # img = Image.fromarray(img2.astype('uint8'))
    # img.show("222")
    # end = time.time()
    # print(f'截图耗时{str(end - start)}')

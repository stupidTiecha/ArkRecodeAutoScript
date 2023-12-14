import os
import numpy as np

from module.base.const import BaseConst
from PIL import Image

from module.base.logger import logger
from module.base.utils import image_size, get_bbox, load_image, get_color

IMPORT_EXP = """from module.base.button import Button

"""
IMPORT_EXP = IMPORT_EXP.strip().split('\n') + ['']


class ButtonExtractor:

    def __init__(self, file, is_debug):
        """
        Args:
            file(str): xxx.png or xxx.gif
        """
        self.name, self.ext = os.path.splitext(file)
        self.area, self.color, self.button, self.file = (), (), (), ''
        self.is_debug = is_debug
        self.load()

    @staticmethod
    def _extract(image, file):
        size = image_size(image)
        if size != (1280, 720):
            logger.warning(f'{file} Image size is not correct: wanted (1280,720) but {size}')
        bbox = get_bbox(image)
        mean = get_color(image, bbox)
        mean = tuple(np.rint(mean).astype(int))
        return bbox, mean

    def load(self):
        file = self.get_file()
        area, color = self._extract(load_image(file), file)
        button = area
        self.area = area
        self.color = color
        self.button = button
        self.file = file

    def get_file(self):
        file = f'{self.name}{self.ext}'
        return os.path.join(BaseConst.BUTTON_IMAGES_FOLDER_DEBUG, file)

    @property
    def expression(self):
        if not self.is_debug:
            self.file = self.file[4:]
        return '%s = Button(area=%s, color=%s, button=%s, file=\'%s\')' % (
            self.name, self.area, self.color, self.button, self.file)


class ModuleExtractor:
    def __init__(self, is_debug=False):
        self.is_debug = is_debug

    @property
    def expression(self):
        exp = []
        for file in get_button_path():
            exp.append(ButtonExtractor(file, self.is_debug).expression)
            logger.info(f'extract Image info : {file}')
        exp = IMPORT_EXP + exp
        return exp

    def write(self):
        file = BaseConst.BUTTON_ASSETS_FILE
        if os.path.exists(file):
            backup = file + '.BAK'
            if os.path.exists(backup):
                os.remove(backup)
                logger.debug(f'remove old backup : {backup}')
            os.rename(file, backup)
            logger.debug(f'rename old {file} to {file} .BAK')
        with open(BaseConst.BUTTON_ASSETS_FILE, 'w', newline='') as file:
            for text in self.expression:
                file.write(text + '\n')


def get_button_path():
    return os.listdir(BaseConst.BUTTON_IMAGES_FOLDER_DEBUG)


if __name__ == '__main__':
    m = ModuleExtractor(is_debug=True)
    m.write()
    """
        for _ in get_button_path():
        # img = Image.open(BaseConst.BUTTON_IMAGES_PATH + _.__str__())
        # img2 = np.array(img)
        # img = img.getchannel(0)
        # print(f'image shape is {img2.shape}', f'size is {img2.size}')
        # print(f'{_} bbox is {img.getbbox()}')
        # img.crop(img.getbbox()).show(_)
        img2 = load_image(BaseConst.BUTTON_IMAGES_PATH + _.__str__())
        bbox1 = get_bbox(img2)
        x1, y1, x2, y2 = map(int, map(round, bbox1))
        h, w = img2.shape[:2]
        border = np.maximum((0 - y1, y2 - h, 0 - x1, x2 - w), 0)
        mean1 = get_color(img2, bbox1)
        logger.debug(f'mean: {mean1}')
        mean1 = tuple(np.rint(mean1).astype(int))
        logger.debug(f'mean after np : {mean1}')
        # x1, y1, x2, y2 = bbox
        logger.debug(f'Border: {border}')
        logger.debug(f'{x1, y1, x2, y2} ---------> {bbox1}')

    """

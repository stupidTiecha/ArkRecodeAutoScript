import os
import numpy as np

from module.base.const import BaseConst
from PIL import Image

from module.base.logger import logger
from module.base.utils import image_size, get_bbox, load_image, get_color


class ButtonExtractor:
    @staticmethod
    def _extract(image, file):
        size = image_size(image)
        if size != (1280, 720):
            logger.warning(f'{file} Image size is not correct: wanted (1280,720) but {size}')
        bbox = get_bbox(image)
        mean = get_color(image, bbox)
        mean = tuple(np.rint(mean).astype(int))
        return bbox, mean


def get_button_path():
    return os.listdir(BaseConst.BUTTON_IMAGES_PATH)


if __name__ == '__main__':
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

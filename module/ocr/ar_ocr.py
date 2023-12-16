import time

from cnocr import CnOcr

from module.base.logger import logger


class ocr(CnOcr):
    def __init__(self,):
        super().__init__()



if __name__ == '__main__':
    img = '../../assets/GAME_VERSION.png'
    # cnocr = CnOcr()
    # out = cnocr.ocr(img,rec_model_name='densenet_lite_136-fc', det_model_name='naive_det', cand_alphabet='0123456789')
    # logger.info(out)
    start = time.time()
    logger.debug('init ocr module')
    oc = CnOcr()
    end = time.time()
    logger.debug(f'ocr module init complete, cost time: {end - start}')
    logger.debug('start ocr image')
    start = time.time()
    out = oc.ocr(img)
    end = time.time()
    logger.debug(f'image ocr complete, cost time: {end - start}')
    logger.info(out)

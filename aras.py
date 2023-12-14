import os.path

import module.assets.assets as a
from module.base.logger import logger


class ArkRecodeAutoScript:
    pass


if __name__ == '__main__':
    file = a.LOG_OUT.raw_file
    logger.debug(os.path.exists(file))

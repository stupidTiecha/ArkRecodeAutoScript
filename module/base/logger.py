import coloredlogs
import logging

logger = logging.getLogger('aras')
coloredlogs.install(level='DEBUG', logger=logger)
# logger.setLevel(logging.DEBUG)
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)




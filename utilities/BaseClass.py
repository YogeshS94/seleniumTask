import inspect
import logging

import pytest


@pytest.mark.usefixtures('setup')
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('log_file.log')
        f = logging.Formatter("%(asctime)s, %(levelname)s, %(name)s, %(message)s")
        fileHandler.setFormatter(f)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
        # self.driver.


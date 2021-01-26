from Lib import ConfigReader
import softest
from Lib.logger import logGen
from Lib.Assertions import Assertion
from Lib import ExcelUtility

runnable_tests = ExcelUtility.runnable_test()


def is_testcase_runnable(testcasename):

    if testcasename in runnable_tests:
        return False
    else:
        return True


class BaseClass(softest.TestCase):
    base_url = ConfigReader.get_base_url()
    symbol = ConfigReader.get_symbol()
    apiKey = ConfigReader.get_api_key()
    logger = logGen.logger()
    global runnable_tests
    assertion = Assertion()



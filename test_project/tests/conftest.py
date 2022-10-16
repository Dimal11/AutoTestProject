import allure
import pytest

from test_env.browser_factory.browser import WebDriver
from test_env.utils.logger import Logger


@pytest.fixture(scope='session')
def driver():
    Logger().get_logger()
    yield WebDriver().get_driver()
    WebDriver().stop_driver()


# @pytest.hookimpl(trylast=True)
# def pytest_configure(config):
#     allure.environment(test_server='testserver', report='My Test Report')

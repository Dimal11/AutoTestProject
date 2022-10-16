import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from test_env.browser_factory import BrowseFactory
from test_env.singleton import Singleton


class WebDriver(metaclass=Singleton):
    def __init__(self):
        self.__driver = BrowseFactory().get_driver()

    def get_driver(self):
        return self.__driver

    def find_element(self, locator: tuple):
        return self.__driver.find_element(*locator)

    def submit(self, locator: tuple):
        return self.find_element(locator).submit()

    def switch_to(self):
        return self.__driver.switch_to

    def stop_driver(self):
        self.__driver.quit()
        self._instances = {}

    def wait(self):
        return WebDriverWait(self.__driver, int(os.getenv('WAITING_TIME')))

    def execute_script(self, script: str):
        return self.__driver.execute_script(script=script)

    def get_action(self):
        return ActionChains(self.__driver)

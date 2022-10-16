import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_env.browser_factory.browser import WebDriver
from abc import ABC


class BaseForm(ABC):

    def __init__(self, uniq_element=None, form_name=None):
        self.uniq_element = uniq_element
        self.form_name = form_name

    def is_page_open(self):
        if WebDriverWait(WebDriver().get_driver(), int(os.getenv('WAITING_TIME'))) \
                .until(EC.presence_of_element_located(self.uniq_element.locator_by)):
            return True
        else:
            return False

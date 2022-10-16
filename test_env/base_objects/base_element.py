from selenium.webdriver.support import expected_conditions as EC

from test_env.browser_factory.browser import WebDriver


class BaseElement:

    def __init__(self, locator_type, locator, element_name):
        self.locator = locator
        self.locator_by = (locator_type, locator)
        self.element_name = element_name

    # FIND
    def _find_element(self):
        element = WebDriver().find_element(self.locator_by)
        return element

    def _find_elements(self):
        elements = WebDriver().get_driver().find_elements(self.locator_by)
        return elements

    def get_element(self):
        return self._find_element()

    # EXPLICIT WAIT

    def wait_to_be_clickable(self):
        return WebDriver().wait().until(EC.element_to_be_clickable(self.locator_by))

    def wait_visibility_of_element_located(self):
        return WebDriver().wait().until(EC.visibility_of_element_located(self.locator_by))

    def wait_invisibility_of_element(self):
        return WebDriver().wait().until(EC.invisibility_of_element(self.locator_by))

    # ---------------------------------------------

    def get_text(self):
        return self._find_element().text

    def is_displayed(self):
        return self._find_element().is_displayed()

    def get_attr(self, attr_name: str):
        return self._find_element().get_attribute(attr_name)

    def submit(self):
        self._find_element().submit()

    def move_to_element(self):
        WebDriver().get_action().move_to_element(self._find_element()).perform()

    def action_click(self):
        WebDriver().get_action().click(self.get_element()).perform()

    def action_send_keys(self, text):
        WebDriver().get_action().click(self.get_element()).perform()
        WebDriver().get_action().send_keys(text).perform()

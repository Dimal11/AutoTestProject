import os

import allure
import pytest

from test_project.page_objects.test_form import TestForm


@allure.feature('Test1')
class Test1:

    @allure.title('Test test')
    def test_1(self, driver):
        try:
            driver.get(os.getenv('URL'))
            with allure.step('Step 1'):
                assert TestForm().is_page_open(), 'Not open'
        except:
            allure.attach(
                driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
            raise

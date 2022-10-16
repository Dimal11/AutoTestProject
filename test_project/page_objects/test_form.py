from test_env.base_objects.base_form import BaseForm
from test_env.base_objects.base_element import BaseElement


class TestForm(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='MainForm',
            uniq_element=BaseElement(
                locator_type='css selector',
                locator='span.mw-headline',
                element_name='FormMainLbl'
            )
        )

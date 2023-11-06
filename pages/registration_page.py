from .base_page import BasePage
from .locators import RegistrationPageLocators
from selenium.webdriver.support.ui import Select


class RegistrationPage(BasePage):

    def should_be_begin_test_button(self):
        assert self.is_element_present(*RegistrationPageLocators.BEGIN_TEST_BUTTON), "Begin test button not on page"

    def should_be_link(self, link):
        assert self.is_element_present(*link), "Link not found on page"

    def should_be_active_begin_button(self):
        begin_test_button = self.browser.find_element(*RegistrationPageLocators.BEGIN_TEST_BUTTON)
        not_active = begin_test_button.get_attribute("disabled")
        assert not_active is None, "Begin test button is disabled"

    def should_be_not_active_begin_button(self):
        begin_test_button = self.browser.find_element(*RegistrationPageLocators.BEGIN_TEST_BUTTON)
        not_active = begin_test_button.get_attribute("disabled")
        assert not_active is not None, "Begin test button is active"

    def fill_text_fields(self, data):
        data_value = [data[key] for key in data]
        for l in range(len(RegistrationPageLocators.DATA)):
            field = self.browser.find_element(*RegistrationPageLocators.DATA[l])
            field.send_keys(data_value[l])

    def check_fields(self):
        for check in RegistrationPageLocators.CHECK:
            mark = self.browser.find_element(*check)
            mark.click()

    def check_with_unmarked_field(self):
        for check in RegistrationPageLocators.CHECK_WITH_UNMARKED_FIELD:
            mark = self.browser.find_element(*check)
            mark.click()

    def select_fields(self):
        country = Select(self.browser.find_element(*RegistrationPageLocators.COUNTRY_FIELD))
        country.select_by_index(5)

    def go_to_begin_test(self):
        begin_test_button = self.browser.find_element(*RegistrationPageLocators.BEGIN_TEST_BUTTON)
        begin_test_button.click()

    def go_to_link(self, link):
        link_on_page = self.browser.find_element(*link)
        link_on_page.click()

from .base_page import BasePage
from .locators import ConfirmationPageLocators


class ConfirmationPage(BasePage):
    def should_be_confirmation_message(self):
        assert self.is_element_present(*ConfirmationPageLocators.CONFIRMATION_MESSAGE), "Confirmation message not found on page"

    def should_be_back_button(self):
        assert self.is_element_present(*ConfirmationPageLocators.BACK_BUTTON), "Back button not found on page"

    def go_to_registration_form(self):
        back_button = self.browser.find_element(*ConfirmationPageLocators.BACK_BUTTON)
        back_button.click()

import pytest

from .pages.registration_page import RegistrationPage

from .pages.confirmation_page import ConfirmationPage

from .pages.locators import RegistrationPageLocators

LINK = "https://uts.sirius.online//#/auth/register/qainternship"


@pytest.mark.positive
def test_user_registration_with_valid_data(browser, user_valid_data):
    page = RegistrationPage(browser, LINK)
    page.open()
    page.fill_text_fields(user_valid_data)
    page.check_fields()
    page.select_fields()
    page.should_be_active_begin_button()
    page.go_to_begin_test()
    confirmation_page = ConfirmationPage(browser, browser.current_url)
    confirmation_page.should_be_confirmation_message()


@pytest.mark.negative
@pytest.mark.parametrize('user_invalid_data', [{'lastname': 'Иванов', 'firstname': 'Иван', 'patronymic': 'Иванович', 'email': 'animator0297@mail.ru',
                                            'voshlogin': '1234', 'phone': '12345', 'snils': '16283465279', 'profession': 'Учитель',
                                            'city': 'Сочи', 'orgname': 'созвездие', 'school': 'школа5', 'grade': '11А'},
                                            {'lastname': 'Иванов', 'firstname': 'Иван', 'patronymic': 'Иванович', 'email': 'animator0297@mail.ru',
                                                'voshlogin': 'v00.000.000', 'phone': '12345', 'snils': '16283465279',
                                                'profession': 'Учитель', 'city': 'Сочи', 'orgname': '', 'school': 'школа5', 'grade': '11А'}])
def test_user_registration_with_invalid_data(browser, user_invalid_data):
    page = RegistrationPage(browser, LINK)
    page.open()
    page.fill_text_fields(user_invalid_data)
    page.check_fields()
    page.select_fields()
    page.should_be_not_active_begin_button()


@pytest.mark.negative
def test_user_registration_with_unmarked_field(browser, user_valid_data):
    page = RegistrationPage(browser, LINK)
    page.open()
    page.fill_text_fields(user_valid_data)
    page.check_with_unmarked_field()
    page.select_fields()
    page.should_be_not_active_begin_button()


@pytest.mark.testlink
@pytest.mark.parametrize('link', [RegistrationPageLocators.AGREEMENT_LINK, RegistrationPageLocators.PROCESS_PERSONAL_DATA_LINK,
                                  RegistrationPageLocators.RULES_LINK])
def test_go_to_link(browser, link):
    page = RegistrationPage(browser, LINK)
    page.open()
    page.should_be_link(link)
    page.go_to_link(link)


def test_go_back_registration_form(browser, user_valid_data):
    test_user_registration_with_valid_data(browser, user_valid_data)
    confirmation_page = ConfirmationPage(browser, browser.current_url)
    confirmation_page.should_be_back_button()
    confirmation_page.go_to_registration_form()

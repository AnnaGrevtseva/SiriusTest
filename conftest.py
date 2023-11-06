import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = chrome_options()
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    elif browser_name == "firefox":
        options = firefox_options()
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()


@pytest.fixture
def user_valid_data():
    data = {'lastname': 'Иванов', 'firstname': 'Иван', 'patronymic': 'Иванович', 'email': 'animator0297@mail.ru',
            'voshlogin': 'v00.000.000', 'phone': '12345', 'snils': '16283465279', 'profession': 'Учитель',
            'city': 'Сочи', 'orgname': 'созвездие', 'school': 'школа5', 'grade': '11А'}
    return data

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='fr', help='Choose from langs: (en-gb/ru/es..)')

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    print ("language is ", user_language)
    yield browser
    print("\nquit browser..")
    browser.quit()

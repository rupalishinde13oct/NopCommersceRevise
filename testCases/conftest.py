import pytest
from selenium import webdriver

@pytest.fixture(params=[
    ("admin@yourstore.com" , "admin" , "Pass"),
    ("admin@yourstor1.com" , "admin" , "Fail"),
    ("admin@yourstore.com" , "admin1", "Fail"),
    ("admin@yourstore1.com" , "admin1", "Fail")
])

def getLoginData(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        print("Launching Chrome browser...!!")
        d = webdriver.Chrome()

    elif browser == 'firefox':
        print("Launching Firefox browser...!!")
        d = webdriver.Firefox()

    elif browser == 'edge':
        print("Launching Edge browser...!!")
        d = webdriver.Edge()

    else:
        print("Headless Mode...!!")
        opt = webdriver.ChromeOptions()
        opt.add_argument("headless")
        d = webdriver.Chrome(options= opt)

    d.maximize_window()
    return d


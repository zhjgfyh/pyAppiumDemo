# encoding: utf-8

import pytest
from appium import webdriver

import config

BASE_SERVER_URL = 'http://localhost:'
port = '4723'
SERVER_URL = BASE_SERVER_URL + port + '/wd/hub'


def get_driver():
    try:
        desired_caps = config.DesiredCaps.desired_caps
        driver = webdriver.Remote(SERVER_URL, desired_caps)
        driver.implicitly_wait(30)
    except Exception as e:
        print("Error:", e)
    finally:
        print("finally...")
    return driver


@pytest.fixture(scope="function")
def driver(request):
    print("start...")
    driver = None
    driver = get_driver()

    def tear_down():
        # end the session
        print("tear down...")
        driver.quit()

    request.addfinalizer(tear_down)
    return driver

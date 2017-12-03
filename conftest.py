# encoding: utf-8

import os
import pytest
from appium import webdriver

import config

BASE_SERVER_URL = 'http://localhost:'
port = '4723'
SERVER_URL = BASE_SERVER_URL + port + '/wd/hub'


@pytest.fixture(scope="function")
def driver(request):
    print("start...")
    desired_caps = config.DesiredCaps.desired_caps
    driver = webdriver.Remote(SERVER_URL, desired_caps)
    driver.implicitly_wait(30)

    def tear_down():
        # end the session
        print("tear down...")
        driver.quit()
    request.addfinalizer(tear_down)
    return driver



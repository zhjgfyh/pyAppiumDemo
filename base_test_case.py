# encoding: utf-8

import os
import pytest
from appium import webdriver

import config


class BaseTestCase():
    @pytest.fixture(scope="function")
    def driver(self, request):
        print("start...")
        desired_caps = config.DesiredCaps.desired_caps
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def tear_down():
            # end the session
            print("tear down...")
            self.driver.quit()

        request.addfinalizer(tear_down)
        return self.driver

    def test_find_elements(self, driver):
        print("test case...")

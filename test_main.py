# encoding: utf-8

import os
import pytest
from appium import webdriver

import config
from base_test_case import *
import time


class TestSimpleAndroid(object):

    def test_find_elements(self, driver):
        # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("test case1...")
        assert driver is not None

    def test_find_elements_sec(self, driver):
        # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("test case2...")
        assert driver is not None

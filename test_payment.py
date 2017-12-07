# encoding: utf-8

import os
import pytest
from appium import webdriver

import config
from base_test_case import *
import time

class TestPayment(object):

    def test_shop(self, driver):
        print("test case3 in another class......")
        # "Shop" page
        # sh = self.driver.find_element_by_xpath("//*[@class='android.view.View' and @index='2']")
        # sh.click()
'''
        # Switch
        print self.driver.contexts
        self.driver.switch_to.context('mWebView')
        print self.driver.current_context
'''
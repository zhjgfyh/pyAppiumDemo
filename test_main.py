# encoding: utf-8

import os
import pytest
from appium import webdriver

import config
from base_test_case import *
import time


class TestSimpleAndroid(object):

    def test_find_elements(self, driver):
        #driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("test case...")
        el = driver.find_element_by_class_name('android.view.View')
        el.click()

        start_btn = driver.find_element_by_id('com.manboker.headportrait:id/clsd_style_btn')
        #camera = driver.find_element_by_id('com.manboker.headportrait:id/comics_main_top_view_to_camera_iv')
        assert start_btn is not None

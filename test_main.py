# encoding: utf-8

import os
import pytest
from appium import webdriver

import config
from base_test_case import *


class TestSimpleAndroid(BaseTestCase):

    def test_find_elements(self, driver):
        print("test case...")
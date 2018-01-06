# encoding: utf-8

from time import sleep

import pytest
import sys

from base_test_case import *
from utils.find_elements import *

'''
pytest单独的存放fixtures的文件
'''


class TestSimpleAndroid(object):

    @pytest.mark.skip(reason="Don't run in debug mode.")
    def test_login(self, driver):
        # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("start to test " + sys._getframe().f_code.co_name)
        assert driver is not None

        login_entry_home = mm_find_element_by_id(driver, "com.manboker.headportrait:id/entry_album_set")
        assert login_entry_home is not None, "用户已经登录"
        login_entry_home.click()

        # mm_find_element_by_id(driver, "com.manboker.headportrait:id/no_message_image").click()
        sleep(3)
        driver.save_screenshot("./screenshot/login.png")

        login_btn = mm_find_element_by_id(driver, "com.manboker.headportrait:id/nologin_retry")
        assert login_btn is not None, "登录按钮不存在"
        login_btn.click()

        send_phone_msg_btn = mm_find_element_by_id(driver, "com.manboker.headportrait:id/set_other")
        assert send_phone_msg_btn is not None, "登录弹框未展示"
        send_phone_msg_btn.click()

        user_name_input = mm_find_element_by_id(driver, "com.manboker.headportrait:id/login_user")
        assert user_name_input is not None, "未找到用户登录框"
        user_name_input.click()
        # user_name_input.set_value('18600274100')
        user_name_input.send_keys('18600274100')

        pwd_input = mm_find_element_by_id(driver, "com.manboker.headportrait:id/login_password")
        assert pwd_input is not None, "未找到密码登录框"
        pwd_input.click()
        # user_name_input.set_value('18600274100')
        pwd_input.send_keys('Jklm,.789')

        login_btn_other = mm_find_element_by_id(driver, "com.manboker.headportrait:id/login_submit")
        assert login_btn_other is not None, "登录按钮未展示"
        login_btn_other.click()
        sleep(3)
        driver.save_screenshot("./screenshot/profile.png")
        self_profile = mm_find_element_by_id(driver, "com.manboker.headportrait:id/specific_user_headicon")
        assert self_profile is not None, "可能未进入profile页面"
        sleep(5)

    def test_logout(self, driver):
        # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("start to test " + sys._getframe().f_code.co_name)
        assert driver is not None

        logout_entry_home = mm_find_element_by_id(driver, "com.manboker.headportrait:id/entry_album_set_icon")
        assert logout_entry_home is not None, "用户还未登录"
        logout_entry_home.click()

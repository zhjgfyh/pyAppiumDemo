# encoding: utf-8

from time import sleep
from base_test_case import *



'''
pytest单独的存放fixtures的文件
'''

class TestSimpleAndroid(object):

    def test_find_elements(self, driver):
        # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("test case1...")
        assert driver is not None
        driver.find_element_by_id("com.manboker.headportrait:id/entry_album_set").click()
        sleep(3)
        driver.save_screenshot("./screenshot/login.png")
        try:
            login_btn = None
            login_btn = driver.find_element_by_id("com.manboker.headportrait:id/nologin_retry")
        except :
            pass
        assert login_btn is not None, "登录按钮不存在"
        login_btn.click()

        try:
            send_phone_msg_btn = None
            send_phone_msg_btn = driver.find_element_by_id("com.manboker.headportrait:id/set_send_code")
        except :
            pass
        assert send_phone_msg_btn is not None, "登录弹框未展示"
        # login_btn.click()

    @pytest.mark.skip(reason="Don't run in debug mode.")
    def test_find_elements_sec(self, driver):
        # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.save_screenshot("./1.png")

# encoding: utf-8

import sys
from time import sleep

from base_test_case import *
from conftest import driver
from utils.find_elements import *

'''
pytest单独的存放fixtures的文件
'''


class TestSimpleAndroid(object):

    #@pytest.mark.skip(reason="Don't run in debug mode.")
    def test_Caricatures(self, driver):
        print("start to test " + sys._getframe().f_code.co_name)
        assert driver is not None

        caris = mm_find_elements_by_class(driver, "android.view.View")
        assert caris is not None, "漫画页未展示"
        caris[0].click()
        sleep(2)

        '''
        skip_camera_btn = mm_find_element_by_id(driver, "com.manboker.headportrait:id/guide_video_close")
        assert skip_camera_btn is not None, "Skip按钮未找到"
        skip_camera_btn.click()

        # For Galaxy_s6
        per_allow_btn = mm_find_element_by_id(driver, 'com.android.packageinstaller:id/permission_allow_button')
        assert per_allow_btn is not None, "授权拍照允许按钮未找到"
        per_allow_btn.click()
        access_allow_btn = mm_find_element_by_id(driver, 'com.android.packageinstaller:id/permission_allow_button')
        assert per_allow_btn is not None, "授权打开照片允许按钮未找到"
        per_allow_btn.click()

        album_btn = mm_find_element_by_id(driver, "com.manboker.headportrait:id/localtion_picture")
        assert album_btn is not None, "Album按钮未找到"
        album_btn.click()

        downloads_folder = mm_find_elements_by_class(driver, "android.widget.RelativeLayout")
        assert downloads_folder is not None, "Downloads文件夾未找到"
        downloads_folder[1].click()
        sleep(10)

        my_albums = mm_find_element_by_id(driver, "com.manboker.headportrait:id/child_image")
        assert my_albums is not None, "图片未找到"
        my_albums.click()

        gender_select = mm_find_element_by_id(driver, "com.manboker.headportrait:id/iv_gender_woman")
        assert gender_select is not None, "女孩图标未找到"
        gender_select.click()

        age_select = mm_find_element_by_id(driver, "com.manboker.headportrait:id/adjust_age_mature_iv")
        assert age_select is not None, "年龄图标未找到"
        age_select.click()

        confirm_btn = mm_find_element_by_id(driver, "com.manboker.headportrait:id/dressing_goback")
        assert confirm_btn is not None, "Confirm按钮未找到"
        confirm_btn.click()

        cate_female = mm_find_element_by_id(driver, "com.manboker.headportrait:id/clsd_item_click_layout")
        assert cate_female is not None, "female分类未找到"
        cate_female.click()

        start_btn = mm_find_element_by_id(driver, "clsd_style_btn")
        assert start_btn is not None, "分类页未展示"
        start_btn.click()
        driver.save_screenshot("./screenshot/cari.png")
        sleep(5)

        tap_page = mm_find_element_by_id(driver, "com.manboker.headportrait:id/guide_change_model_head_anim_view")
        tap_page = mm_find_element_by_id(driver, "com.manboker.headportrait:id/finger_text")
        assert tap_page is not None, "页面无法点击"
        tap_page.click()
        
        go_to_camera_btn = mm_find_element_by_id(driver, "comics_main_top_view_to_camera_iv")
        assert go_to_camera_btn is not None, "拍照按钮未找到"
        go_to_camera_btn.click()
        sleep(2)
        
        '''

        number_of_people = mm_find_element_by_id(driver, "comic_filter_init_layout")
        assert number_of_people is not None, "筛选按钮未找到"
        number_of_people.click()

        one_people = mm_find_element_by_id(driver, "comic_filter_dialog_pone_text")
        assert one_people is not None, "无法选一人"
        one_people.click()

        filter_confirm = mm_find_element_by_id(driver, "button1")
        assert filter_confirm is not None, "确定按钮未找到"
        filter_confirm.click()

        face_edit_btn = mm_find_element_by_id(driver, "dress_iv")
        assert face_edit_btn is not None, "美妆按钮未找到"
        face_edit_btn.click()
        sleep(1)

        glass_btn = mm_find_element_by_id(driver, "select_glasses_fl")
        assert glass_btn is not None, "眼镜选项未找到"
        glass_btn.click()
        sleep(1)

        select_glass = mm_find_elements_by_class(driver, "android.widget.RelativeLayout")
        assert select_glass is not None, "第四款眼镜未找到"
        select_glass[4].click()
        sleep(2)

        dressing_confirm = mm_find_element_by_id(driver, "dressing_goback")
        assert dressing_confirm is not None, "美妆确认按钮未找到"
        driver.save_screenshot("./screenshot/addGlass.png")
        dressing_confirm.click()

    @pytest.mark.skip(reason="Don't run in debug mode.")
    def test_Emoticons(self, driver):
        print("start to test " + sys._getframe().f_code.co_name)
        assert driver is not None

        emos = mm_find_elements_by_class(driver, 'android.view.View')
        assert emos is not None, "表情页未展示"
        emos[1].click()

        search_btn = mm_find_element_by_id(driver, "com.manboker.headportrait:id/action_edit")
        assert search_btn is not None, "搜索按钮未找到"
        search_btn.click()

        input_keywords = mm_find_element_by_id(driver, "com.manboker.headportrait:id/search_src_text")
        assert input_keywords is not None, "关键字输入框未找到"
        #input_keywords.click()
        input_keywords.send_keys('love')
        driver.press_keycode(66)
        sleep(5)
        driver.save_screenshot("./screenshot/searchLove.png")

        searchResult = mm_find_elements_by_class(driver, "android.widget.LinearLayout")
        assert searchResult is not None, "表情Heart未找到"
        searchResult[8].click()

        saveGif = mm_find_elements_by_class(driver, "android.widget.RelativeLayout")
        assert saveGif is not None, "保存Gif按钮未找到"
        saveGif[1].click()
        sleep(5)
        driver.save_screenshot("./screenshot/saveGif.png")

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

        #send_phone_msg_btn = mm_find_element_by_id(driver, "com.manboker.headportrait:id/set_other")
        #assert send_phone_msg_btn is not None, "登录弹框未展示"
        #send_phone_msg_btn.click()

        user_name_input = mm_find_element_by_id(driver, "com.manboker.headportrait:id/login_user")
        assert user_name_input is not None, "未找到用户登录框"
        #user_name_input.clear()
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

    @pytest.mark.skip(reason="Don't run in debug mode.")
    def test_logout(self, driver):
        # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("start to test " + sys._getframe().f_code.co_name)
        assert driver is not None

        logout_entry_home = mm_find_element_by_id(driver, "com.manboker.headportrait:id/entry_album_set_icon")
        assert logout_entry_home is not None, "用户还未登录"
        logout_entry_home.click()

        self_profile = mm_find_element_by_id(driver, "com.manboker.headportrait:id/specific_user_headicon")
        assert self_profile is not None, "可能未进入profile页面"
        self_profile.click()

        logout_btn = mm_find_element_by_id(driver, "com.manboker.headportrait:id/set_log_in_text")
        assert logout_btn is not None, "退出登录按钮未找到"
        logout_btn.click()

        confirm_btn = mm_find_element_by_id(driver, "android:id/button1")
        assert confirm_btn is not None, "确定按钮未找到"
        confirm_btn.click()

        sleep(2)

    @pytest.mark.skip(reason="Don't run in debug mode.")
    def test_payment(self, driver):
        # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("start to test " + sys._getframe().f_code.co_name)
        assert driver is not None, "Driver is not available."

        sleep(3)
        homepage_entries = mm_find_elements_by_class(driver, "android.view.View")
        assert homepage_entries[2] is not None, "shop entry is not available."
        homepage_entries[2].click()
        sleep(5)

        print(driver.contexts)
        print(driver.current_context)
        driver.switch_to.context('WEBVIEW_0')
        print(driver.current_context)
        sleep(5)


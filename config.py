# encoding: utf-8

app_caps_aoyou = {
    'appPackage': 'com.aoyou.android',
    'appActivity': '.view.common.MainActivity',
    'appWaitActivity': '.view.common.MainActivity'
}

app_caps_moman = {
    'appPackage': 'com.manboker.headportrait',  # 包名
    'appActivity': '.activities.SplashActivity',  # launcher activity
    'appWaitActivity': '.activities.EntryActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True
}

samsung_s7 = {
    'platformName': 'Android',
    'version': '6.0.1',
    'deviceName': 'SM_G9350',
    'udid': '6a1ca77c'
}

huawei_7i = {
    'platformName': 'Android',
    'version': '6.0.1',
    'deviceName': 'HUAWEI ATH_AL00',
    'udid': '69T7N15A31016757'
}


class DesiredCaps:
    desired_caps = {}
    desired_caps = dict(samsung_s7, **app_caps_moman)
    desired_caps['deviceReadyTimeout'] = 100
    desired_caps['newCommandTimeout'] = 120


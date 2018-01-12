# encoding: utf-8

app_caps_aoyou = {
    'appPackage': 'com.aoyou.android',
    'appActivity': '.view.common.MainActivity',
    'appWaitActivity': '.view.common.MainActivity'
}

app_caps_moman = {
    'appPackage': 'com.manboker.headportrait',  # 包名
    'appActivity': '.activities.SplashActivity',  # launcher activity
    'appWaitActivity': '.activities.EntryActivity'
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

Nexus = {
    'platformName': 'Android',
    'version': '4.3',
    'deviceName': '192.168.140.101:5555'
}


samsung_s6 = {
    'platformName': 'Android',
    'version': '7.0',
    'deviceName': 'SM_G920T',
    'udid': '04157df4d349751c'
}

class DesiredCaps:
    desired_caps = {}
    desired_caps = dict(samsung_s6, **app_caps_moman)
    desired_caps['deviceReadyTimeout'] = 100
    desired_caps['newCommandTimeout'] = 120
    desired_caps['unicodeKeyboard'] = "True"
    desired_caps['resetKeyboard'] = "True"
    desired_caps['noReset'] = "True"

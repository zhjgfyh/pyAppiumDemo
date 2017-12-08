#encoding: utf-8
app_caps_aoyou={
    'appPackage' : 'com.aoyou.android', #包名
    'appActivity' : '.view.common.MainActivity',#launcher activity
    'appWaitActivity' : '.view.common.MainActivity'
}
app_caps_moman = {
    'appPackage' : 'com.manboker.headportrait', #包名
    'appActivity' : '.activities.FirstActivity',#launcher activity
    'appWaitActivity' : '.activities.EntryActivity'
}
samsung_s7 = {
    'platformName':'Android',
    'version' : '6.0.1',
    'deviceName':'SM_G9350',
    'udid':'6a1ca77c'
}
class DesiredCaps:
    desired_caps={}
    desired_caps = dict(samsung_s7, **app_caps_moman)
    desired_caps['deviceReadyTimeout'] = 100
    desired_caps['newCommandTimeout'] = 120
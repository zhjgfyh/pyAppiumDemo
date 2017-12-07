#encoding: utf-8

samsung_s7 = {
    'platformName':'Android',
    'version' : '6.0.1',
    'deviceName':'SM_G9350',
    'udid':'6a1ca77c'
}
class DesiredCaps:
    desired_caps={}
    desired_caps = samsung_s7
    # for value in samsung_s7:
    #     desired_caps[value] = samsung_s7[value]
    # desired_caps['app'] = PATH(
    #     '../../../sample-code/apps/ApiDemos/bin/ApiDemos-debug.apk'
    # )
    desired_caps['appPackage'] = 'com.aoyou.android' #包名
    desired_caps['appActivity'] = '.view.common.MainActivity'#launcher activity
    desired_caps['appWaitActivity'] = '.view.common.MainActivity'
    desired_caps['deviceReadyTimeout'] = 100
    desired_caps['newCommandTimeout'] = 120
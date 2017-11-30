#encoding: utf-8


class DesiredCaps:
    desired_caps={}
    desired_caps['platformName'] = 'Android' #平台
    desired_caps['platformVersion'] = '5.1.1' #android版本
    desired_caps['deviceName'] = 'MI_4' #手机devicename
    desired_caps['udid'] = '11e898e2' #手机udid
    # desired_caps['app'] = PATH(
    #     '../../../sample-code/apps/ApiDemos/bin/ApiDemos-debug.apk'
    # )
    desired_caps['appPackage'] = 'com.aoyou.android' #包名
    desired_caps['appActivity'] = '.view.common.MainActivity'#launcher activity
    desired_caps['appWaitActivity'] = '.view.common.MainActivity'
    desired_caps['deviceReadyTimeout'] = 100
    desired_caps['newCommandTimeout'] = 120
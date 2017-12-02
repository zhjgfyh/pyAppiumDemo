#encoding: utf-8


class DesiredCaps:
    desired_caps={}
    desired_caps['platformName'] = 'Android' #平台
    desired_caps['platformVersion'] = '4.3' #android版本
    desired_caps['deviceName'] = '192.168.56.101:5555' #手机devicename
    # desired_caps['udid'] = '11e898e2' #手机udid
    # desired_caps['app'] = PATH(
    #     '../../../sample-code/apps/ApiDemos/bin/ApiDemos-debug.apk'
    # )
    desired_caps['appPackage'] = 'com.manboker.headportrait' #包名
    desired_caps['appActivity'] = '.activities.SplashActivity'#launcher activity
    desired_caps['appWaitActivity'] = '.activities.EntryActivity'
    desired_caps['deviceReadyTimeout'] = 100
    desired_caps['newCommandTimeout'] = 120
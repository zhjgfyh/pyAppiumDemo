#-*-coding:utf-8-*-

import socket

# 自动启动Appium server


def start_service():
    print("start appium server...")
    # to do


def stop_service():
    print("stop appium server...")
    # to do


def service_cmds():
    pass
    # if '-1'!= udid:
    # to do


def is_appium_running():
    return False


def find_free_port():
    """
    函数返回值是当前可用来监听的一个随机端口,int
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    # 用getsockname来获取我们实际绑定的端口号
    addr, port = s.getsockname()
    # 释放端口
    s.close()
    return port


if __name__ == '__main__':
    print(str(find_free_port()))

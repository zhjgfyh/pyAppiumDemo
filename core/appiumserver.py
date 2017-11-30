# encoding: utf-8
import socket


def find_free_port():
    """
    函数返回值是当前可用来监听的一个随机端口。
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    # 用getsockname来获取我们实际绑定的端口号
    addr, port = s.getsockname()
    # 释放端口
    s.close()
    return port


if __name__ == '__main__':
    print(find_free_port())

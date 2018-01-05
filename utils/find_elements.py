# encoding: utf-8

"""
    寻找控件封装
"""


def mm_find_element_by_id(driver, element_id):
    """
      按id寻找控件
    """
    element = None
    try:
        element = driver.find_element_by_id(element_id)
    except:
        pass
    return element
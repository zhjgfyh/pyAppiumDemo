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
    except Exception as e:
        pass
    return element


def mm_find_elements_by_class(driver, class_name):
    elements = None
    try:
        elements = driver.find_elements_by_class_name(class_name)
    except:
        pass
    return elements


def switch_to_webdriver(driver):
    pass
# import pytest
# from selenium import webdriver
#
# @pytest.fixture(scope='package',autouse=True)
# def st_emptyEnv():
#     """打开浏览器并登录"""
#     print('打开浏览器')
#     wd = webdriver.Chrome()
#     wd.implicitly_wait(5)
#
#     print('管理员登录')
#     wd.get('http://127.0.0.1/mgr/sign.html')
#     wd.find_element_by_id('username').send_keys('byhy')
#     wd.find_element_by_id('password').send_keys('88888888')
#     wd.find_element_by_tag_name('button').click()
#
#     yield
#
#     wd.quit()







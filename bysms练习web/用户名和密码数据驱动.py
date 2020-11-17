from lib.bysms练习web.loginAndCheck import *
import pytest
from lib.bysms练习web.conftest import *
from selenium import webdriver
import time
from lib.bysms练习web.登录封装 import driver

class Test_login测试:
    name = '管理员用户名密码测试'

    @pytest.mark.parametrize('username,password,expectedalert', [
        (None, '88888888', '请输入用户名'),
        ('byhy', None, '请输入密码'),
        ('byh', '88888888', '登录失败 : 用户名或者密码错误'),
        ('byhy', '888888888', '登录失败 : 用户名或者密码错误'),
        ('byhy', '8888888', '登录失败 : 用户名或者密码错误')
    ])
    def test_001_005(self,username,password,expectedalert):
        alertText = loginAndCheck(username,password)
        assert alertText == expectedalert

class Test_管理员操作:
    name = '管理员操作测试'

    def test_UI_0101(self):
        print('菜单栏检查测试')
        sidebarMenu = driver.find_element_by_class_name('sidebar-menu')
        elements = sidebarMenu.find_elements_by_tag_name('span')
        eles = []
        for ele in elements:
            eles.append(ele.text)

        assert eles[:3] == ['客户','药品','订单']

    def test_UI_0102(self):
        print('添加客户并检查客户测试')
        #找到输入框
        driver.find_element_by_class_name('glyphicon-plus').click()
        inputs = driver.find_element_by_class_name('add-one-area') \
                    .find_elements_by_class_name('form-control')

        #输入框输入
        inputs[0].send_keys('南京中医院')
        inputs[1].send_keys('15684235864')
        inputs[2].send_keys('南京市中山北路')

        driver.find_element_by_class_name('add-one-area') \
                .find_element_by_class_name('btn-xs').click()

        Menu = driver.find_element_by_class_name('search-result-item')
        spans = Menu.find_elements_by_tag_name('span')
        Text = []
        for span in spans:
            Text.append(span.text)

        expected = ['客户名：','南京中医院','联系电话：','15684235864','地址：','南京市中山北路']
        assert Text == expected

    def test_UI_0103(self):
        print('点击链接并返回测试')
        driver.find_element_by_css_selector('[href="http://www.python3.vip"]').click()
        #保存当前窗口句柄
        mainWindow = driver.current_window_handle

        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if '白月黑羽教python' in driver.title:
                break

        eles = driver.find_element_by_class_name('d-md-inline-flex') \
                    .find_elements_by_tag_name('span')

        Titles = [ele.text for ele in eles]
        expected = ['Python基础', 'Python进阶', '图形界面', 'Web开发', '自动化测试', '性能测试', '常见问题', '其它']
        assert Titles == expected

        #返回到原来的窗口
        driver.switch_to.window(mainWindow)
        driver.find_element_by_class_name('user-image').click()
        #点击退出登录
        driver.find_element_by_class_name('user-footer') \
                .find_element_by_class_name('pull-right').click()
        #一定要引入强制等待，因为退出有一个时间
        time.sleep(2)

        url = driver.current_url
        assert url == 'http://127.0.0.1/mgr/sign.html'
        driver.quit()



























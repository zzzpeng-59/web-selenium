from selenium import webdriver
import time

def loginAndCheck(username,password):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    url = 'http://127.0.0.1/mgr/sign.html'
    driver.get(url)

    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('password').clear()

    if username is not None:
        driver.find_element_by_id('username').send_keys(username)
    if password is not None:
        driver.find_element_by_id('password').send_keys(password)

    driver.find_element_by_tag_name('button').click()

    time.sleep(3)
    alertText = driver.switch_to.alert.text
    print('用户名密码测试')
    driver.quit()

    return alertText



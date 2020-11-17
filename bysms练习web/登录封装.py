from selenium import webdriver
import time

def DRIVER():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    url = 'http://127.0.0.1/mgr/sign.html'
    driver.get(url)
    driver.find_element_by_id('username').send_keys('byhy')
    driver.find_element_by_id('password').send_keys('88888888')
    driver.find_element_by_tag_name('button').click()
    time.sleep(3)
    return driver

driver = DRIVER()



from selenium import  webdriver
driver = webdriver.Chrome()
driver.get('http://127.0.0.1/mgr/sign.html')
print(driver.title)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.cowin.gov.in/')
driver.find_element('name', 'email').send_keys('shubham3414')
driver.implicitly_wait(3000)

print(driver.title)
driver.close()
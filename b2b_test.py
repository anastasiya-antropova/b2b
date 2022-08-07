from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import time

link = ('https://b2b.cloud-test.renlife.com')
browser = webdriver.Chrome()
browser.get(link)
time.sleep(3)

#authorization
login=browser.find_element(By.CSS_SELECTOR,'.el-input [name=username]').send_keys("akbb.testb2b2")
password=browser.find_element(By.NAME,'password').send_keys("akbb.testb2b2")
#login=browser.find_element(By.CSS_SELECTOR,'.el-input [name=username]').send_keys("test.b2b")
#password=browser.find_element(By.NAME,'password').send_keys("test.b2b")
go=browser.find_element(By.CSS_SELECTOR,'.form__actions>.el-button').click()
time.sleep(3)

#choice_of_channel
channel=browser.find_element(By.CSS_SELECTOR, '.el-form-item:nth-child(2) .el-input__suffix-inner').click()
time.sleep(1)
#channel_rozn=browser.find_element(By.CSS_SELECTOR, 'body>div:nth-child(4)>div>div>ul>li:nth-child(1)')
channel_rozn=browser.find_element(By.CSS_SELECTOR, 'li:nth-child(1)')
time.sleep(1)
channel_rozn.click()
#select=Select(browser.find_element(By.TAG_NAME,"ul"))
#select.select_by_visible_text('Розница')

time.sleep(15)
browser.quit()

base_sum=browser.find_element(By.NAME, "base_sum")
base_sum.send_keys(random.randint(50000,1000000))


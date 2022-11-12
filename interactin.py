from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:/Users/grase/Downloads/chromedriver_win32/chromedriver"

driver= webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

count=driver.find_element(By.CSS_SELECTOR,"#articlecount a")
print(count.text)
all_portals= driver.find_element(By.LINK_TEXT,"1982 Embassy World Snooker Championship")
# all_portals.click()

search =driver.find_element(By.NAME,"search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

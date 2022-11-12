from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:/Users/grase/Downloads/chromedriver_win32/chromedriver"

driver= webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

name=driver.find_element(By.NAME,"fName")
surname=driver.find_element(By.NAME,"lName")
email=driver.find_element(By.NAME,"email")

name.send_keys("Peter")
surname.send_keys("Petrovsky")
email.send_keys("peter321@centrum.sk")

signup=driver.find_element(By.CSS_SELECTOR,"button")
signup.click()

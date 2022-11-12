from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_path="C:/Users/grase/Downloads/chromedriver_win32/chromedriver"
driver=webdriver.Chrome(executable_path=chrome_path)
driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

name=driver.find_element(By.ID,"username")
surname=driver.find_element(By.ID,"password")
name.send_keys("rasevovakarolina@gmail.com")
surname.send_keys("kolinkolin")


log_in=driver.find_element(By.XPATH,"/html/body/div/main/div[3]/div[1]/form/div[3]/button")
log_in.click()
driver.get("https://www.linkedin.com/jobs/search/")


all_jobs= driver.find_elements(By.CSS_SELECTOR,"job-card-container--clicable")
for job in all_jobs:
    print("called")
    job.click()

    try:
        




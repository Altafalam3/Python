username= input("Enter your username :")
password= input("Enter your password :")


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://instagram.com")
time.sleep(5)
def search():
   user=driver.find_element(By.XPATH , '//*[@id="loginForm"]/div/div[1]/div/label/input')
   user.send_keys(username)
   time.sleep(2)

   pswd=driver.find_element(By.XPATH , '//*[@id="loginForm"]/div/div[2]/div/label/input')
   pswd.send_keys(password)
   time.sleep(2)

   submit=driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
   submit.click()
   time.sleep(5)

search()
input()

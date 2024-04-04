""" Program to speed up and facilitate the meeting of people """ 
 
from selenium import webdriver 
from time import time  
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchAttributeException

EMAIL_FACEBOOK = "Your email login"  
PASS_FACEBOOK = "Your pass" 

chrome_driver_path = "code driver path"
driver = webdriver.Chrome(executable_path=chrome_driver_path) 

driver.get("http://www.tinder.com") 

sleep(2) 
button_login = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button') 
button_login.click() 

sleep(2) 
facebook_login = driver.find_element_by_parth('//*[@id="modal-manager]/div/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
facebook_login.click() 
 
sleep(2) 
window = driver_window_handles[0] 
facebook_window_login = driver.window_handles[1] 
driver.switch_to.window(facebook_window_login) 
print(driver.title)
 
email = driver.find_element_by_xpath('//*[@id="email"]') 
password = driver.find_element_by_xpath('//*[@id="pass"]') 
email.send_keys(EMAIL_FACEBOOK) 
password.send_keys(PASS_FACEBOOK) 
password.send_keys(Keys, ENTER) 

driver.switch_to.window(window) 
print(driver.title) 

sleep(5) 
 
loc_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]') 
loc_button.click()  
not_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]') 
not_button.click() 
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button') 
cookies.click()  

for n in range(100): 
    sleep(1) 

    try: 
        print("Called")  
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button') 
        like_button.click() 

    except ElementClickInterceptedException: 
       sleep(2)
 
driver.quit()

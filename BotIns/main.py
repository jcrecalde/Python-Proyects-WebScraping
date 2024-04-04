""" Bot follows instagram """  
""" The account part uses the account of your interest """ 

from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time

ACCOUNT = "inverarg" 
INS_USERNAME = "Your user name" 
INS_PASS = "Your pass"   

class InsFollower: 
     
    def __init__(self): 
        chrome_options = webdriver.ChromeOptions() 
        chrome_options.add_experimental_option("detach", True) 
        self.driver = webdriver.Chrome(options=chrome_options) 

    def login(self): 
        url = "https://www.instagram.com/accounts/login/" 
        self.driver.get(url) 
        time.sleep(5) 

        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie = self.driver.find_elements(By.XPATH, decline_cookies_xpath) 

        if cookie: 
            cookie[0].click() 

        username = self.driver.find_element(by=By.NAME, value="username") 
        password = self.driver.find_element(by=By.NAME, value="password") 

        username.send_keys(INS_USERNAME)  
        password.send_keys(INS_PASS) 

        time.sleep(2.1) 
        password.send_keys(Keys.ENTER) 

        time_sleep(4.5)  

        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click() 

        time.sleep(3.7)
        
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()


     
    def find_followers(self): 
        time.sleep(5) 

        self.driver.get(f"https://www.instagram.com/{ACCOUNT}/followers") 

        time.sleep(5.5) 

        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self): 
        all_button = self.driver.find_element(By.CSS_SELECTOR, value="._aano button") 

        for button in all_button:  
            try:
                button.click() 
                time.sleep(1.5)  
            except ElementClickInterceptedException:  
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]") 
                cancel_button.click()



bot = InsFollower() 
bot.login() 
bot.find_followers()
bot.follow()



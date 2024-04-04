""" Bot to send information to Twitter about the download and upload speed """   
from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time

INET_PROMISED_DOWN = 150 
INET_PROMISED_UP = 10 
CHROME_DRIVER_PATH = "your diver path" 
TW_EMAIL = "your email"  
TW_PASS = "your pas"

class InetSpeedTwBot: 
    def __init__(self, driver_path): 
        self.driver = webdriver.Chrome() 
        self.up = 0 
        self.down = 0 
     
    def get_inet_speed(self): 
        self.driver.get("https://www.speedtest.net/es") 

        time.sleep(3) 

        start_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a") 
        start_button.click() 

        time.sleep(60) 
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text 
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tw_at_provider(self): 
        self.driver.get("https://twitter.com/login") 
         
        time.sleep(3) 
        email = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input') 
        password = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input') 
         
        email.send_keys(TW_EMAIL) 
        password.send_keys(TW_PASS)  
        time.sleep(2) 
        password.send_keys(Keys.ENTER) 

        time.sleep(3) 
        tw_compose = self.driver.find_element(by.XPATH, value='(//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div') 
         
        tw = f"why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"  
        tw_compose.send_keys(tw) 
        time.sleep(4)  

        tw_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tw_button.click()  

        time.sleep(3) 
        self.driver.quit()



        
bot = InetSpeedTwBot()
bot.get_inet_speed() 
bot.tw_at_provider()
"""
This code automates the production and purchase of cookies in a game or web experiment over a 5-minute period, displaying the number of cookies produced per second at the end of the period.""" 
 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()
    if time.time() > timeout: 

        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        prices_items = [] 

        for price in all_prices:
            t_element = price.text
            if t_element  != "":
                cost = int(t_element .split("-")[1].strip().replace(",", ""))
                prices_items.append(cost)

        up_cookies= {}
        for n in range(len(item_prices)):
            up_cookies[prices_items[n]] = item_ids[n]

        element_money = driver.find_element(by=By.ID, value="money").text
        if "," in element_money:
            element_money = element_money.replace(",", "")
        cookie_count = int(element_money) 

        affordable_upgrades = {}
        for cost, id in cup_cookies.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_afford_up = max(affordable_upgrades)
        print(highest_afford_up)
        to_purchase_id = affordable_upgrades[highest_afford_up]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        timeout = time.time() + 5

    
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
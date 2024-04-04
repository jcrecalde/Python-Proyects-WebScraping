from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

EMAIL_ACCOUNT = "jcrecalde30@gmail.com" 
PASSW_ACCOUNT = ""  
PHONE = ""
 
chrome = webdriver.ChromeOptions() 
chrome.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=chrome) 

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
) 

time.sleep(2) 
sign_button = driver_find_element(by=By.LINK_TEXT, value="Sign in") 
sign_button.click() 

time.sleep(5) 
 
email = driver.find_element(by=By.ID, value="username") 
email.send_keys(EMAIL_ACCOUNT)  
password = driver.find_element(by=By.ID, value="password") 
password.send_keys(PASSW_ACCOUNT) 
password.send_keys(keys, ENTER) 
 
input("Press Enter") 

time.sleep(5)
all_list = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for list in all_list:
    print("Opening List")
    list.click()
    time.sleep(2)
    try:
        
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Application Complete, skipped.")
            continue
        else:
            print("Submit job application")
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
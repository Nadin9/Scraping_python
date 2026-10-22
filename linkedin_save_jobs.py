from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3720876208&distance=25&f_AL=true&geoId=91000001&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER')

time.sleep(2)
# sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")

# click the sign in widget
sign_in_button = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in_button.click()

time.sleep(2)
# sign in
fill_email = driver.find_element(By.ID, value="username")
fill_email.send_keys("nadinmusa99@gmail.com")

fill_password = driver.find_element(By.ID , value="password")
fill_password.send_keys("Lovemeright99")

sign_in = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
sign_in.click()
# sign_in.send_keys("Keys.ENTER")

time.sleep(2)

# Jobs list
# jobs=driver.find_elements(By.CLASS_NAME, value='ember-view')
jobs=driver.find_elements(By.CLASS_NAME, value='job-card-container--clickable')
        

time.sleep(2)

for i in jobs[ :4]:
    i.click()
    time.sleep(1)
    save_button = driver.find_element(By.CLASS_NAME,value='jobs-save-button')
    save_button.click()
   
# abort_application()
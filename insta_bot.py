from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "nadinmusa99@gmail.com"
PASSWORD = 'Callmebaby99'

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach',True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.instagram.com/')

    def login(self):

        fill_email = self.driver.find_element(By.NAME, value="username")
        fill_email.send_keys(EMAIL)

        fill_password = self.driver.find_element(By.NAME , value="password")
        fill_password.send_keys(PASSWORD)
        fill_password.send_keys(Keys.ENTER)

        time.sleep(10)
        self.driver.get('https://www.instagram.com/')

        #notif Not Now
        time.sleep(9)
        self.driver.find_element(By.XPATH, value="/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()

    def send_messages(self):
        # go_to_messages
        self.driver.get("https://www.instagram.com/direct/t/115689056481425/")

        time.sleep(11)

        message =self.driver.find_element(By.CLASS_NAME, value='x1gh3ibb')
        message.send_keys("Hello Hello", Keys.ENTER) 


bot = InstaFollower()
time.sleep(2)
bot.login()
time.sleep(4)
bot.send_messages()
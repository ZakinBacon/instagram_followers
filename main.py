from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import requests
import os

load_dotenv()
chrome_drive_path = r"C:\Users\Zach\Desktop\chromedriver_win32\chromedriver.exe"
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

class Instagram:
    def __init__(self, driver_path):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options, service=Service(executable_path=driver_path, log_path="NUL"))
        self.followers = []
        self.following = []
    def instagram_login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        self.instagram_username = self.driver.find_element(By.CSS_SELECTOR, 'input[class="_aa4b _add6 _ac4d"]')
        self.instagram_username.send_keys(INSTAGRAM_USERNAME)
        time.sleep(1)
        self.instagram_password = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Password"]')
        self.instagram_password.send_keys(INSTAGRAM_PASSWORD)
        time.sleep(1)
        self.instagram_password.send_keys(Keys.ENTER)
        time.sleep(3)

    def get_follower_count(self, account_name):
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{account_name}/followers/")
        time.sleep(3)
        self.background_selector = self.driver.find_element(By.CSS_SELECTOR, 'div[class="x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"]')
        time.sleep(1)
        self.background_selector.click()
        time.sleep(1)
        for x in range(0,20):
            self.background_selector.send_keys(Keys.PAGE_DOWN)

        self.followers = self.driver.find_elements(By.CSS_SELECTOR, 'span[class="_aacl _aaco _aacw _aacx _aad7 _aade"]')
        for follower in self.followers:
            print(follower.text)
        pass


bot = Instagram(chrome_drive_path)
bot.instagram_login()
bot.get_follower_count(INSTAGRAM_USERNAME)
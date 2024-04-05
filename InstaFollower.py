from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import msvcrt
from selenium.common.exceptions import ElementClickInterceptedException
import os



INSTAGRAM_EMAIL = os.environ.get("email")
INSTAGRAM_PASSWORD = os.environ.get("password")
INSTAGRAM_USERNAME = os.environ.get("username")


class InstaFollower:
    def __init__(self):
        # self.target_account = input("Enter the username of target account: ")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.instagram.com')

    def login(self):


        # time.sleep(5)
        # press_login = self.driver.find_element(By.LINK_TEXT, 'Log In').click()

        time.sleep(5)
        login_email = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Phone number, username, or email"]')
        login_email.send_keys(INSTAGRAM_EMAIL)
        time.sleep(2)
        login_password = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Password"]')
        login_password.send_keys(INSTAGRAM_PASSWORD, Keys.ENTER)

        # time.sleep(5)
        # home = self.driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Home"]').click()
        time.sleep(5)
        not_now_popup = self.driver.find_element(By.CSS_SELECTOR, '._ac8f div').click()
        time.sleep(10)

    def find_followers(self):
        time.sleep(5)
        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'followers').click()


        time.sleep(5)
        modal = self.driver.find_element(By.CLASS_NAME, '_aano') #modal is the xpath of the dialog box containing the scrolling list
        time.sleep(5)

        for i in range(1):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, '._aano button')    # taking a class up toch and using the next button. please see pictures in project folder for reference
        print(len(all_buttons))


        for button in all_buttons:
            try:
                button.click()
                time.sleep(5)
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]').click()








    def follow(self):
        pass



















from selenium import webdriver
# to auto the web broser to do what ever task we need to acomplish
import os
#  for basic folder or path manipulation
import time
#  to keep track of time for any time based process we want to do


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # browser to login to instagram
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.login()
        
    #  go to instagram login page
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login')
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)


if __name__ == '__main__':
    #  instance of the class
    ig_bot = InstagramBot('temp_username', 'temp_password')
    print(ig_bot.username)
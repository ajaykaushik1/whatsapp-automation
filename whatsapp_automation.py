# selenium basics
# {
# browser.get("https://www.selenium.dev")
# download = browser.find_element_by_link_text("Downloads")
# download.click()
# search = browser.find_element_by_id("")
# search.send_keys("downloads")
# }

# Whatsapp Automation

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
browser = webdriver.Chrome(
    "C:/Users/lenovo/Desktop/whatsapp automation/chromedriver")
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 10000)
# name = input("enter receiver name")
target = '"receiver_name"'

# file_path = input("enter the file path")
# file_path = "C:/Users/lenovo/Desktop/whatsapp automation/image.jpg"
# string = input("enter message")
string = "Test Message"
x_arg = '//span[contains(@title, ' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()
input_box = browser.find_element_by_class_name('DuUXI')
# print("enter number of time's the mssg send")
# x= int(input("enter number"))
for i in range(10):
    input_box.send_keys(string + Keys.ENTER)

# attachment_section = browser.find_element_by_xpath('//div[@title = "Attach"]')
# attachment_section.click()
#
# image_box = browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
# image_box.send_keys(file_path)
#
# sleep(3)
#
send_button = browser.find_element_by_xpath('//span[@data-icon="send-light"]')
send_button.click()

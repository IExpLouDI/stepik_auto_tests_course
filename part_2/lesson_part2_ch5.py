import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
link = "http://suninjuly.github.io/file_input.html"

with webdriver.Chrome() as driver:
	driver.get(link)
	driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys("name")
	driver.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys("lastname")
	driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("email@.com")
	driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(file_path)
	driver.find_element(By.CSS_SELECTOR, ".btn").click()
	time.sleep(5)

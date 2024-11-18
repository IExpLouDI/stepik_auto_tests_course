from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
import time


link: str = "http://suninjuly.github.io/find_link_text"
key_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

driver: WebDriver

with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
	driver.get(link)
	link1 = driver.find_element(By.LINK_TEXT, value=key_text)
	link1.click()

	input1: WebElement = driver.find_element(By.TAG_NAME, "input")
	input1.send_keys("Ivan")
	input2 = driver.find_element(By.NAME, "last_name")
	input2.send_keys("Petrov")
	input3 = driver.find_element(By.CLASS_NAME, "form-control.city")
	input3.send_keys("Smolensk")
	input4 = driver.find_element(By.ID, "country")
	input4.send_keys("Russia")
	button = driver.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()
	time.sleep(30)
	driver.quit()

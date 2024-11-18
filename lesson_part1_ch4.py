from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/huge_form.html"

with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
	driver.get(link)
	elements = driver.find_elements(By.TAG_NAME, "input")

	for element in elements:
		element.send_keys("Test word")

	button = driver.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()

	time.sleep(15)
	driver.quit()

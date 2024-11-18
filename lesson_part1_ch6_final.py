# Для работы кода, требуется выполнить команду pip install webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
links = [link1, link2]

with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
	for link in links:
		driver.get(link)
		input_1 = driver.find_element(By.CSS_SELECTOR, "div.first_block input.first.form-control")
		input_1.send_keys("Test_1")
		input_2 = driver.find_element(By.CSS_SELECTOR, "div.first_block input.second.form-control")
		input_2.send_keys("Test_2")
		input_3 = driver.find_element(By.CSS_SELECTOR, "div.first_block input.third.form-control")
		input_3.send_keys("Test_3")

		input_4 = driver.find_element(By.CSS_SELECTOR, "div.second_block input.first")
		input_4.send_keys("Test_4")
		input_5 = driver.find_element(By.CSS_SELECTOR, "div.second_block input.second")
		input_5.send_keys("Test_5")

		button_1 = driver.find_element(By.CSS_SELECTOR, "button.btn")
		button_1.click()

		time.sleep(3)

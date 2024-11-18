from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
options = Options()
options.add_experimental_option("detach", True) # что бы браузер не закрывался

with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as browser:
	browser.get(link)
	input1: WebElement = browser.find_element(By.TAG_NAME, "input")
	input1.send_keys("Ivan")
	input2 = browser.find_element(By.NAME, "last_name")
	input2.send_keys("Petrov")
	input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
	input3.send_keys("Smolensk")
	input4 = browser.find_element(By.ID, "country")
	input4.send_keys("Russia")
	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()
	time.sleep(30)
	browser.quit()

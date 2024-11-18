from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
	#ожидание появления элемента
	driver.implicitly_wait(5)
	driver.get("http://suninjuly.github.io/wait1.html")
	driver.find_element(By.ID, "verify").click()
	message = driver.find_element(By.ID, "verify_message")
	assert "successful" in message.text

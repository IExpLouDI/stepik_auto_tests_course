from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def get_result(value:str)->str:
	return str(math.log(abs(12*math.sin(int(value)))))


with webdriver.Chrome() as driver:

	link = "http://suninjuly.github.io/explicit_wait2.html"
	driver.get(link)
	waiter = WebDriverWait(driver, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "100")
	)

	driver.find_element(By.ID, "book").click()

	value = driver.find_element(By.CSS_SELECTOR, "#input_value").text
	result_math = get_result(value)
	driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(result_math)
	driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
	print(driver.switch_to.alert.text.split(": ")[-1])

	# из урока
	# driver.get("http://suninjuly.github.io/wait2.html")
	# driver.find_element(By.ID, "button")

	# button = WebDriverWait(driver, 5).until(
	# 	EC.element_to_be_clickable((By.ID, "verify"))
	# )
	# button.click()
	# message = driver.find_element(By.ID, "verify_message")
	# assert "successful" in message.text

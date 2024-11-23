import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


link = "http://suninjuly.github.io/selects2.html"

with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
	driver.get(link)
	selects = driver.find_elements(By.CSS_SELECTOR, "h2 span")
	result = str(sum([int(val.text) for val in selects if val.text.isdigit()]))
	select = Select(driver.find_element(By.CSS_SELECTOR, "#dropdown"))
	select.select_by_value(result)
	driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
	time.sleep(6)

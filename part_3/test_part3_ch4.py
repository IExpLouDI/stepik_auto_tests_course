import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
	with webdriver.Chrome() as driver:
		driver.get("http://selenium1py.pythonanywhere.com/")
		with pytest.raises(NoSuchElementException):
			driver.find_element(By.CSS_SELECTOR, "button.btn")
			pytest.fail("Не должно быть кнопки Отправить")

def test_exception2():
	with webdriver.Chrome() as driver:
		driver.get("http://selenium1py.pythonanywhere.com/")
		with pytest.raises(NoSuchElementException):
			driver.find_element(By.CSS_SELECTOR, "no_such_button.btn")
			pytest.fail("Не должно быть кнопки Отправить")

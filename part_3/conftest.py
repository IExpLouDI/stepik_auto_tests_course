#	Для хранения часто употребимых фикстур и хранения глобальных настроек
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
	print("\nStart browser for test\n")
	driver = webdriver.Chrome()
	yield driver
	print("Closed browser. \n")
	driver.quit()

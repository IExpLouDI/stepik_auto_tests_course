import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"


# все метки должны быть описаны в файле pytest.ini расположенного в корневой директории
@pytest.fixture(scope="function")
def driver():
	print("\nstart browser for test...\n")
	driver = webdriver.Chrome()
	yield driver
	print("\nquite driver...\n")
	driver.close()


class TestMainPage1:

	@pytest.mark.smoke
	def test_guest_should_see_login_link(self, driver):
		driver.get(link)
		driver.find_element(By.CSS_SELECTOR, "#login_link")

	@pytest.mark.regression
	def test_guest_should_see_basket_link_on_the_main_page(self, driver):
		driver.get(link)
		driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLinks(unittest.TestCase):

	def test_1(self):
		link1 = "http://suninjuly.github.io/registration1.html"
		with webdriver.Chrome() as driver:
			driver.get(link1)
			driver.find_element(By.CSS_SELECTOR, "div.first_block input.first.form-control").send_keys("Test_1")
			driver.find_element(By.CSS_SELECTOR, "div.first_block input.second.form-control").send_keys("Test_1")
			driver.find_element(By.CSS_SELECTOR, "div.first_block input.third.form-control").send_keys("Test_1")
			driver.find_element(By.CSS_SELECTOR, "button.btn").click()
			result = driver.find_element(By.TAG_NAME, "h1").text
			self.assertEqual(result, "Congratulations! You have successfully registered!")


	def test_2(self):
		link2 = "http://suninjuly.github.io/registration2.html"
		with webdriver.Chrome() as driver:
			driver.get(link2)
			driver.find_element(By.CSS_SELECTOR, "div.first_block input.first.form-control").send_keys("Test_1")
			driver.find_element(By.CSS_SELECTOR, "div.first_block input.second.form-control").send_keys("Test_1")
			driver.find_element(By.CSS_SELECTOR, "div.first_block input.third.form-control").send_keys("Test_1")
			driver.find_element(By.CSS_SELECTOR, "button.btn").click()
			result = driver.find_element(By.TAG_NAME, "h1").text
			self.assertEqual(result, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
	unittest.main()

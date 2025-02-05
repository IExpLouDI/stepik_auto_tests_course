#	Для хранения часто употребимых фикстур и хранения глобальных настроек
# PyTest автоматически находит и подгружает файлы conftest.py, которые находятся в директории с тестами.
# Если вы храните все свои скрипты для курса в одной директории, будьте аккуратны и следите, чтобы не возникало
# ситуации, когда вы запускаете тесты из директории проекта. Рекомендуется, для каждой директории свой отдельный файл
# conftest.py


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

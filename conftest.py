import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Remote("http://standalone:4444/wd/hub", options=webdriver.ChromeOptions())
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

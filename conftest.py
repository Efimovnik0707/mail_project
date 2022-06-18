import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser firefox for test...")
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)    
    yield browser
    print("\nquit browser...")
    browser.quit()

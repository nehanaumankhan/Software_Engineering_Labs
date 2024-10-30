import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup_browser():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_page_conditions(setup_browser):
    driver = setup_browser

    # Open the Django webpage (replace 'example.com' with your local Django page)
    driver.get("http://127.0.0.1:8000/")

    # Define conditions
    a = 2
    b = 3
    c = 4
    d = 3

    # Check the specific conditions and perform actions/assertions
    if a < b:
        if c > d:
            # Find the main heading element and verify its text as an example
            heading = driver.find_element(By.TAG_NAME, "h1")
            assert heading.text == "Welcome to My Demo Website for Selenium Web Automation And Testing Task", \
                "Test Failed: Unexpected heading text."
            print("Test Passed: Conditions are met, and heading text is as expected.")
        else:
            print("Condition `c > d` failed.")
    else:
        print("Condition `a < b` failed.")

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time  # Importing time for delay

@pytest.fixture
def setup_browser():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Define the test cases
Test_Cases = [
    (2, 3, 4, 3),
    (5, 5, 7, 7),
    (8, 6, 7, 7),
    (1, 1, 1, 1)
]

@pytest.mark.parametrize("a, b, c, d", Test_Cases)
def test_page_conditions(setup_browser, a, b, c, d):
    driver = setup_browser

    # Open the local HTML file 
    driver.get("file:///C:/Users/Tesla%20Laptops/OneDrive/Desktop/Software_Engineering_Labs-1/SE_LAB_8/index.html")
    
    # Add a delay to allow the page to process the form and show the result
    time.sleep(10)  # Wait for 2 seconds to see the result before performing assertions
    # Interact with the form and input fields
    driver.find_element(By.ID, "inputA").clear()  # Clear the input fields before entering new values
    driver.find_element(By.ID, "inputA").send_keys(str(a))
    driver.find_element(By.ID, "inputB").clear()
    driver.find_element(By.ID, "inputB").send_keys(str(b))
    driver.find_element(By.ID, "inputC").clear()
    driver.find_element(By.ID, "inputC").send_keys(str(c))
    driver.find_element(By.ID, "inputD").clear()
    driver.find_element(By.ID, "inputD").send_keys(str(d))
    # Add a delay to allow the page to process the form and show the result
    time.sleep(10)  # Wait for 2 seconds to see the result before performing assertions
    # Click the condition checking button
    driver.find_element(By.ID, "condition-check-btn").click()

    

    # Check the specific conditions and perform actions/assertions
    if a < b:
        if c > d:
            result = driver.find_element(By.ID, "result")
            assert "Condition a < b and c > d is true" in result.text
        elif c == d:
            result = driver.find_element(By.ID, "result")
            assert "Condition a < b and c == d is true" in result.text
        else:
            result = driver.find_element(By.ID, "result")
            assert "Condition a < b and c < d is true" in result.text
    elif a == b:
        if c > d:
            result = driver.find_element(By.ID, "result")
            assert "Condition a == b and c > d is true" in result.text
        elif c == d:
            result = driver.find_element(By.ID, "result")
            assert "Condition a == b and c == d is true" in result.text
        else:
            result = driver.find_element(By.ID, "result")
            assert "Condition a == b and c < d is true" in result.text
    else:
        result = driver.find_element(By.ID, "result")
        assert "Condition a > b" in result.text

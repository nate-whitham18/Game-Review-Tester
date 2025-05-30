from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def test_submit_review_form():
    # Path to your local HTML file (adjust path accordingly)
    file_path = f"file://{os.path.abspath('UI-Tests/game_review_form.html')}"

    # Set up the WebDriver (make sure you have the correct driver installed)
    driver_path = os.path.abspath('Drivers/chromedriver-canary.exe')  # or 'chromedriver.exe' on Windows
    # driver_path = os.path.abspath('Drivers/chromedriver-chrome.exe') 

    # Initialize the WebDriver (Chrome example)
    driver = webdriver.Chrome()  # or webdriver.Firefox()

    try:
        driver.get(file_path)  # Adjust path to your HTML file
        driver.maximize_window()

        # Fill out the form fields
        driver.find_element(By.ID, "gameId").send_keys("1")
        driver.find_element(By.ID, "rating").send_keys("5")
        driver.find_element(By.ID, "comment").send_keys("Amazing game!")

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Wait for the message to update
        time.sleep(1)  # simple wait; for more robust tests, use explicit waits

        # Verify success message
        message = driver.find_element(By.ID, "message").text
        assert message == "Review submitted successfully!"
    finally:
        driver.quit()

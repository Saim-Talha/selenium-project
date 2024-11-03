import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def setup_function():
    global driver  # Declare driver as global before assignment

    # Set up the Remote WebDriver
    hub_url = "http://172.17.0.1:4444/wd/hub"
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.binary_location = "/usr/bin/google-chrome"  # Set to the Chrome binary path on the node

    # Initialize the Remote WebDriver
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)

    driver.get('https://stage.alnafi.com/auth/sign-in')
    driver.maximize_window()
    time.sleep(10)

def mycred():
    return [
        ("test1@gmail.com", "test1234"),
        ("test2@gmail.com", "test1234"),
        ("test3@gmail.com", "test1234")
    ]

@pytest.mark.parametrize("username,password", mycred())
def test_login(username, password):
    print("my test login")
    driver.find_element(By.NAME, "email").send_keys(username)
    time.sleep(5)
    driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="my_alanfi_sc", attachment_type=AttachmentType.PNG)

def teardown_function():
    global driver  # Ensure teardown references the global driver
    driver.quit()


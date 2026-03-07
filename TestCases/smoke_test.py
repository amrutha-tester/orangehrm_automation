from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Setup the Chrome Driver automatically
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. Open the OrangeHRM Demo site
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# 3. Validation: Print the page title to the console
print(f"The page title is: {driver.title}")

# 4. Wait for 3 seconds so you can see it worked
time.sleep(3)

# 5. Close the browser
driver.quit()
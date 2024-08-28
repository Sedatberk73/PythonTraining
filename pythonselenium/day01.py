from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button.orangehrm-login-button").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed. The actual title = " + act_title)
    # End the script immediately after printing the failure message
    quit()  # or you can use `sys.exit()` if you have imported `sys`

slider=driver.find_element(By.XPATH,"//p[text()='Buzz Latest Posts']").text
print(slider)
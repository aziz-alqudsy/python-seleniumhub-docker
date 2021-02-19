from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
  command_executor='http://localhost:4000/wd/hub',
  desired_capabilities={
    'browserName': 'chrome',
    'javascriptEnabled': True
  }
)

driver.get("https://ruangguru.com")

print(driver)

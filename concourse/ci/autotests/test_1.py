#file test_1.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys

driver = webdriver.Remote(
   command_executor="http://34.77.6.248/wd/hub",
   desired_capabilities={
            "browserName": "firefox",
            "platform": "LINUX"
        })
print ("Video: "  + driver.session_id)

try:
    driver.implicitly_wait(30)
    #driver.maximize_window() # Note: driver.maximize_window does not work on Linux selenium version v2, instead set window size and window position like driver.set_window_position(0,0) and driver.set_window_size(1920,1080)

    driver.get("https://pcf-demo-reflective-hippopotamus.cfapps.io/")
    driver.get("https://pcf-demo-reflective-hippopotamus.cfapps.io/services")
    driver.add_cookie({"name": "zaleniumMessage", "value": "Going to the database page"})
    elem = driver.find_element_by_id("emailAddress")
    elem.send_keys("tester@gopivotalio")
    elem = driver.find_element_by_id("firstName")
    elem.send_keys("Test")
    elem = driver.find_element_by_id("lastName")
    elem.send_keys("Drone")

    elem = driver.find_element_by_xpath("//*[contains(text(), 'Add')]")
    elem.click()

    driver.add_cookie({"name": "zaleniumMessage", "value": "Added the entry"})
    time.sleep(5)


except:
    driver.add_cookie({"name": "zaleniumTestPassed", "value": "false"})
    driver.quit()
    sys.exit("There was an error, please check the logs")
finally:
    driver.add_cookie({"name": "zaleniumTestPassed", "value": "true"})
    driver.quit()

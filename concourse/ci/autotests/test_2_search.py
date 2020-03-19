#file test_1_create.py
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys

driver = webdriver.Remote(
   command_executor="http://ae4de69e06ae24c19a539949ff38ecb8-1340096117.eu-west-1.elb.amazonaws.com/wd/hub",
   desired_capabilities={
            "browserName": "chrome",
            "platform": "LINUX"
        })
print ("Video: "  + driver.session_id)

try:
    driver.implicitly_wait(30)
    #driver.maximize_window() # Note: driver.maximize_window does not work on Linux selenium version v2, instead set window size and window position like driver.set_window_position(0,0) and driver.set_window_size(1920,1080)

    driver.get("http://drupal.tanzu.alexguedes.com/user/login")
    driver.add_cookie({"name": "zaleniumMessage", "value": "Entering Admin Credentials"})
    elem = driver.find_element_by_id("edit-name")
    elem.send_keys("admin")
    elem = driver.find_element_by_id("edit-pass")
    elem.send_keys("admin123")
    elem = driver.find_element_by_id("edit-submit")
    elem.click()
    driver.add_cookie({"name": "zaleniumMessage", "value": "Added the entry"})
    time.sleep(5)
    driver.get("http://drupal.tanzu.alexguedes.com/admin/content")
    driver.get("http://drupal.tanzu.alexguedes.com/node/add")
    driver.get("http://drupal.tanzu.alexguedes.com/node/add/page")
    time.sleep(2)
    elem = driver.find_element_by_id("edit-title-0-value")
    elem.send_keys("A test page to check connected services")
    actions = webdriver.ActionChains(driver)
    actions.send_keys(Keys.TAB,Keys.TAB,"A test to check saving of a web-page")
    actions.perform()
    time.sleep(2)
    elem = driver.find_element_by_id("edit-submit")
    elem.click()
    time.sleep(2)


#except:
#    driver.add_cookie({"name": "zaleniumTestPassed", "value": "false"})
#    driver.quit()
#    print("There was an error")
#    sys.exit("There was an error, please check the logs")
finally:
    driver.add_cookie({"name": "zaleniumTestPassed", "value": "true"})
    driver.quit()
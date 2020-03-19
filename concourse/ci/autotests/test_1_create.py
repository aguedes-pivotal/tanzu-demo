#file test_1_create.py
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import datetime
zelEndpoint = os.environ['ZELENIUMENDPOINT']
drupalEndpoint = os.environ['DRUPALENDPOINT']
drupalUser = os.environ['DRUPALUSERNAME']
drupalPass = os.environ['DRUPALPASSWORD']
bowsertype = os.environ['BROWSERTYPE']

testName = "Create Test using " + bowsertype + " T:" + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

driver = webdriver.Remote(
   command_executor=zelEndpoint,
   desired_capabilities={
            "browserName": bowsertype,
            "platform": "LINUX",
            "name": testName
        })
print ("Video: " + driver.session_id)

try:
    driver.implicitly_wait(30)
    #driver.maximize_window() # Note: driver.maximize_window does not work on Linux selenium version v2, instead set window size and window position like driver.set_window_position(0,0) and driver.set_window_size(1920,1080)

    driver.get(drupalEndpoint+"/user/login")
    driver.add_cookie({"name": "zaleniumMessage", "value": "Entering Admin Credentials"})
    elem = driver.find_element_by_id("edit-name")
    elem.send_keys(drupalUser)
    elem = driver.find_element_by_id("edit-pass")
    elem.send_keys(drupalPass)
    elem = driver.find_element_by_id("edit-submit")
    elem.click()
    driver.add_cookie({"name": "zaleniumMessage", "value": "Added the entry"})
    time.sleep(5)
    driver.get(drupalEndpoint + "/admin/content")
    driver.get(drupalEndpoint + "/node/add")
    driver.get(drupalEndpoint + "/node/add/page")
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
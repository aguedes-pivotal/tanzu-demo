#file test_1_create.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import datetime
import urllib
import sys

zelEndpoint = os.environ['ZELENIUMENDPOINT']
drupalEndpoint = os.environ['DRUPALENDPOINT']
drupalUser = os.environ['DRUPALUSERNAME']
drupalPass = os.environ['DRUPALPASSWORD']
browsertype = os.environ['BROWSERTYPE']

testName = "Delete test using " + browsertype + " T:" + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")


time.sleep(10)
for i in range(1, 10):
    try:

        driver = webdriver.Remote(
            command_executor=zelEndpoint + "/wd/hub",
            desired_capabilities={
                "browserName": browsertype,
                "platform": "LINUX",
                "name": testName
            })
    except:
        print("Could not connect to zelenium endpoint Retry (%d/10)", i)
        time.sleep(10)

print("Live view of test can be found here: " + zelEndpoint + "/grid/admin/live")

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
    time.sleep(2)
    elem = driver.find_element_by_id("edit-title")
    elem.send_keys("Test Page -" + browsertype)
    elem = driver.find_element_by_id("edit-submit-content")
    elem.click()
    time.sleep(2)
    elements = driver.find_elements_by_tag_name('a')
    found = False
    for elem in elements:
        if "Test Page -" + browsertype in elem.text:
            found = True
            parent = elem.find_element_by_xpath('..').find_element_by_xpath('..')
            checkbox = parent.find_element_by_class_name("form-checkbox")
            checkbox.click()

    if found == False:
        driver.add_cookie({"name": "zaleniumTestPassed", "value": "false"})
        sys.exit("Could not find element")
    else:
        elem = driver.find_element_by_id("edit-submit")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_id("edit-submit")
        elem.click()
        time.sleep(1)
        driver.add_cookie({"name": "zaleniumTestPassed", "value": "true"})
except Exception as E:
   driver.add_cookie({"name": "zaleniumTestPassed", "value": "false"})
   print("There was an error" + E)
   driver.quit()
   sys.exit("There was an error, please check the logs")
   print("See test result" + zelEndpoint + "/dashboard/?q=" + urllib.parse.quote(testName))
finally:
    print ("See test result " + zelEndpoint + "/dashboard/?q=" + urllib.parse.quote(testName))
    print ("See all tests " + zelEndpoint + "/dashboard/")
    driver.quit()
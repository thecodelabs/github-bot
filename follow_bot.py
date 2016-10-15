import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


reload(sys)
sys.setdefaultencoding('utf-8')

# Tell the Python bindings to use Marionette.
caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True


#Firefox used
driver = webdriver.Firefox(capabilities=caps)


# base url
driver.get("http://github.com/login")

username = driver.find_element_by_id("login_field")
password = driver.find_element_by_id("password")

# password and username need to go into these values
username.send_keys("your_user_name_goes_here")
time.sleep(1)
password.send_keys("your_password_goes_here")
time.sleep(1)


login_form = driver.find_element_by_xpath("//input[@value='Sign in']")
time.sleep(1)
login_form.click()
time.sleep(1)

prepend = ["jashkenas", "ruanyf", "substack", "kennethreitz", "jlord", "daimajia", "mdo", "schacon", "mattt",
           "sindresorhus", "defunkt", "douglascrockford", "mbostock", "jeresig",
"mojombo", "addyosmani", "paulirish", "vczh", "romannurik", "tenderlove", "chriscoyier", "johnpapa", "josevalim",
           "charliesome", "CoderMJLee", "ry", "antirez", "muan", "isaacs", "angusshire",
"hadley", "hakimel", "yyx990803", "fat", "fabpot", "ibireme", "tekkub",
           "BYVoid", "laruence", "onevcat", "tpope", "mrdoob", "LeaVerou", "chrisbanes", "wycats", "lifesinger",
"cloudwu", "mitsuhiko", "michaelliao", "ryanb", "clowwindy", "JacksonTian", "yinwang0", "Trinea",
           "pjhyett", "dhh", "gaearon"]


for user in prepend:
    for t in range(1, 100):
        string = "https://github.com/{}/followers?page={}".format(user, t)
        driver.get(string)
        time.sleep(1)

        # make sure to pick the correct directory to save the files to
        follow_button = driver.find_elements_by_xpath("//button[@type='submit']")
        # follow_button = driver.find_elements_by_xpath("//button[@aria-label='Follow this person']")

        # time.sleep(1)
        print len(follow_button)
        try:
            for i in follow_button:
                i.submit()
        except:
            pass
        time.sleep(1)

driver.close()

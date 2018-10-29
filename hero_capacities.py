import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import os

# You need to install chromedriver using the link provided below
# https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/
# install brew
# sudo easy_install selenium
# then "brew install chromedriver"
# specifying the path of the chrome driver
browser = webdriver.Chrome('/usr/local/bin/chromedriver')

# put the website to be opened here
browser.get("http://www.dota2.com/hero/earthshaker/")

print("came here")
keywords = browser.find_element_by_id("heroBioRoles")
print("crossed")
print(type(keywords))
print(keywords)
print(keywords.text)

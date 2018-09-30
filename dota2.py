import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
from time import sleep
import os
import json

browser = webdriver.Chrome('/Users/srividhyaprakash/Downloads/chromedriver')

hero_dict = {}
with open('heroes.json') as json_data:
	d = json.load(json_data)


s = ""
for dicts in d["heroes"]:
	s = "http://www.dota2.com/hero/" + dicts["name"] + "/"
	browser.get(s)
	words = browser.find_element_by_id("heroBioRoles")
	hero_dict[dicts["name"]] = [x.strip() for x in words.text.split("-")]
	dicts["skills"] = hero_dict[dicts["name"]]


print(hero_dict)
d = json.dumps(d, indent = 4)
with open("heroes_modified.json", "w") as open_file:
	open_file.write(d)
browser.close()
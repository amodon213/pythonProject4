import requests
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/alexz/Downloads/chromedriver")
driver.get('https://www.google.com')
driver.find_element_by_name("q").send_keys("cat")
results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
results.click()


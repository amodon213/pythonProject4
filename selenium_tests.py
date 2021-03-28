from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="/Users/alexz/Downloads/chromedriver")
driver.get('https://www.google.com')
driver.find_element_by_name("q").send_keys("cat")
#driver.find_element_by_name("btnK").submit()
test = driver.find_elements_by_xpath('//input[@type="submit"]')
driver.quit()
print(len(test))
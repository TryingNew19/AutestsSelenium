from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")
    browser.find_element_by_id("button").click()
finally:
    time.sleep(30)
    browser.quit()
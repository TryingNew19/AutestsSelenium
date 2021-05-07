from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name("trollface").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector('[type = "submit"]').click()


finally:
    time.sleep(30)
    browser.quit()

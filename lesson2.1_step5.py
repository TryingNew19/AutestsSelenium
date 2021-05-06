from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    checkbox.click()
    radiobtn = browser.find_element_by_css_selector('[for="robotsRule"]')
    radiobtn.click()
    btn = browser.find_element_by_class_name('btn-default')
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
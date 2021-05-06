from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element_by_id("num1").text
    number2 = browser.find_element_by_id("num2").text
    sum = int(number1) + int(number2)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(sum))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
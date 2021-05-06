from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('[name="firstname"]').send_keys("Roman")
    browser.find_element_by_css_selector('[name="lastname"]').send_keys("Romanov")
    browser.find_element_by_css_selector('[name="email"]').send_keys("Romanov@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_new.txt')
    element = browser.find_element_by_css_selector('[name="file"]')
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
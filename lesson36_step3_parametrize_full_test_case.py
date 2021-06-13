import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def answer_func():
    answer = math.log(int(time.time()))
    return answer

#21.207411172357745

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

arr_link = ["https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"]

@pytest.mark.parametrize('links', arr_link)
def test_guest_should_see_login_link(browser, links):
    global final_answ
    link = links
    browser.get(link)
    # time.sleep(3)
    text_field = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ember-text-area"))
    )
    # text_field = browser.find_element_by_class_name("ember-text-area")
    keys_answer = answer_func()
    text_field.send_keys(str(keys_answer))
    button = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "submit-submission"))
    )
    # button = browser.find_element_by_class_name("submit-submission")
    button.click()
    # time.sleep(5)
    feedback = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    assert feedback.text == "Correct!", feedback.text
    browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
import time


def summary(a):
    return log(abs(12 * sin(a)))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(link)
    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_btn = driver.find_element_by_id("book").click()
    x = driver.find_element_by_id("input_value")
    x_text = int(x.text)
    y = str(summary(x_text))
    field = driver.find_element_by_id("answer")
    field.send_keys(y)
    submit_btn = driver.find_element_by_id("solve").click()
    answer = driver.switch_to.alert
    answer_text = answer.text
    answer_num = answer_text.split(': ')[-1]
    print(answer_num)


finally:
    time.sleep(7)
    driver.quit()




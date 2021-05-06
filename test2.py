from selenium import webdriver
from math import log, sin


def summary(a):
    return log(abs(12 * sin(a)))


#  modal window testing
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)
    btn = driver.find_element_by_css_selector(".btn.btn-primary").click()
    confirm = driver.switch_to.alert
    confirm.accept()
    x = int(driver.find_element_by_id("input_value").text)
    y = str(summary(x))
    answer = driver.find_element_by_id("answer").send_keys(y)
    submit_btn = driver.find_element_by_css_selector(".btn.btn-primary").click()

finally:
    driver.quit()





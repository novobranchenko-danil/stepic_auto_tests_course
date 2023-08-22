import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    find_x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    browser.find_element(By.ID, "answer").send_keys(calc(find_x))
    for selector in ["#robotCheckbox", "#robotsRule", ".btn"]:
        browser.find_element(By.CSS_SELECTOR, selector).click()
finally:
    time.sleep(15)
    browser.quit()

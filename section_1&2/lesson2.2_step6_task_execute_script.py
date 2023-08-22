import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Firefox()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser.get(link)
    find_x = calc(browser.find_element(By.ID, "input_value").text)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, "answer").send_keys(find_x)
    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()
finally:
    time.sleep(15)
    browser.quit()

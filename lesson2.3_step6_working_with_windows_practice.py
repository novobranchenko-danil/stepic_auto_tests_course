import time
import math
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "trollface").click()

    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)
    #можно строки 16-17 записать в следующем виде
    browser.switch_to.window(browser.window_handles[1])

    find_x = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(find_x)
    browser.find_element(By.CLASS_NAME, "btn").click()
    alert = browser.switch_to.alert.text
    addAlertToClip = alert.split(': ')[-1]
    pyperclip.copy(addAlertToClip)
finally:
    time.sleep(5)
    browser.quit()

import math
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()
    find_x = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.NAME, "text").send_keys(find_x)
    browser.find_element(By.ID, "solve").click()
    alert = browser.switch_to.alert.text
    addAlertToClip = alert.split(': ')[-1]
    pyperclip.copy(addAlertToClip)
finally:
    time.sleep(3)
    browser.quit()

import time
import math
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn").click()
    browser.switch_to.alert.accept()                            #ереключаемся на алерт и жмем "принять"
    find_x = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(find_x)
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    #чтоб самому не копировать текст, интересная практика
    alert = browser.switch_to.alert.text                        #получаем текст из финального алерта с кодом ответа
    addAlertToClip = alert.split(': ')[-1]                      #получаем последний элемент текста (наш код ответа)
    pyperclip.copy(addAlertToClip)                              #загоняем его в буфер обмена
finally:
    time.sleep(10)
    browser.quit()
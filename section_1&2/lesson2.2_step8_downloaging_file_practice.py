import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__)) #определяем пусть до папки, где лежит файл lesson2.2_step7...
file_path = os.path.join(current_dir, "les2.2_step8.txt")        #добавляем в путь нужный файл, теперь он найдет его

try:
    browser.get(link)
    list_elements = browser.find_elements(By.CLASS_NAME, "form-control") #находим все поля для заполнения
    list_answer = ["Danil", "Ivanov", "test@test.ru"]                    #список текста которым заполняем поля
    for i, element in enumerate(list_elements):                          #в цикле проходимся по полям
        element.send_keys(list_answer[i])                                #и заполняем текстом из списка
    #другой вариант записи в строках 11-14
    #browser.find_element(By.NAME, "firstname").send_keys("Danil")
    #browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
    #browser.find_element(By.NAME, "email").send_keys("test@test.ru")
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
finally:
    time.sleep(10)
    browser.quit()

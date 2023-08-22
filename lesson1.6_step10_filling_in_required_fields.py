from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    label = browser.find_elements(By.TAG_NAME, "label") #ищем все элементами с названиями полей (заголовки над полями)
    _input = browser.find_elements(By.TAG_NAME, "input") #ищем все поля для заполнения

    for i, k in enumerate(label): #в цикле пробегаемся по всем заголовкам. где i начинается с 0, а k имеет название элемента
        k = k.text                #копируем в k текст из текущего элемента
        if k[-1] == "*":          #если последний символ в тексте текущего элемента *, тогда...
            _input[i].send_keys("random text") #... тогда в это поле вставляем "рандом текст"
    #вместо кода выше можно было найти отдельно каждое поле с * и ввести туда текст. Но так меньше строчек
    time.sleep(10)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text  #запишем это условие сразу в 33 строку

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text_elt.text

    #добавим себе в консоль отчет о корректности действий
    if "Congratulations! You have successfully registered!" == welcome_text_elt.text:
        print('Awesome! You have filled in all required fields!')
    else:
        print('something went wrong')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
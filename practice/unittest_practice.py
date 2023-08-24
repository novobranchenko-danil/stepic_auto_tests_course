import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUnittest(unittest.TestCase):

    def test_link1(self):
        try:
            browser = webdriver.Firefox()
            link_1 = "http://suninjuly.github.io/registration1.html"
            browser.get(link_1)
            # Ищем и заполняем обязательные поля
            browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']") \
                .send_keys("Danil")
            browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']") \
                .send_keys("Ivanov")
            browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']") \
                .send_keys("test@ololo.ru")
            time.sleep(3)
            # Ищем кнопку отправки и отправляем форму
            browser.find_element(By.CSS_SELECTOR, "button.btn").click()
            # Ожидаем загрузки страницы
            # Проверяем, что смогли зарегистрироваться
            time.sleep(3)
            # Находим элемент, содержащий текст об успешной регистрации
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt.text,
                             "Something went wrong ")
        finally:
            browser.quit()

    def test_link2(self):
        try:
            browser = webdriver.Firefox()
            link_2 = "http://suninjuly.github.io/registration2.html"
            browser.get(link_2)
            # Ищем и заполняем обязательные поля
            browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']") \
                .send_keys("Danil")
            browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']") \
                .send_keys("Ivanov")
            browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']") \
                .send_keys("test@ololo.ru")
            time.sleep(3)
            # Ищем кнопку отправки и отправляем форму
            browser.find_element(By.CSS_SELECTOR, "button.btn").click()
            # Ожидаем загрузки страницы
            # Проверяем, что смогли зарегистрироваться
            time.sleep(3)
            # Находим элемент, содержащий текст об успешной регистрации
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt.text,
                             "Something went wrong ")
        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()

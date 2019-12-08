from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока цена не упадет
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    button = browser.find_element_by_id("book")
    button.click()


    #Получаем значение X
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    #Вводим ответ
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("#solve")
    button.click()


    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)

finally:
    
    # закрываем браузер после всех манипуляций
    browser.quit()

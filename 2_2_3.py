from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значение 
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    res = str(int(x)+int(y))

    #Выбираем ответ
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(res)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)

finally:
    
    # закрываем браузер после всех манипуляций
    browser.quit()

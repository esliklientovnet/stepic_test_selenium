from selenium import webdriver
import time
import math
import os 


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

   

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    browser.switch_to.window(browser.window_handles[1])


    #Получаем значение X
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    #Вводим ответ
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)

finally:
    
    # закрываем браузер после всех манипуляций
    browser.quit()

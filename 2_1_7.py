from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значение X
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    #Вводим ответ
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    #robotCheckbox
    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()

    #robotsRule
    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
finally:
    
    # закрываем браузер после всех манипуляций
    browser.quit()

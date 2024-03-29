from selenium import webdriver
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector("input[name=firstname]")
    first_name.send_keys("first_name")

    last_name = browser.find_element_by_css_selector('input[name=lastname]')
    last_name.send_keys("last_name")

    email = browser.find_element_by_css_selector('input[name=email]')
    email.send_keys("email")

    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = os.path.join(current_dir, 'file.txt') 
    file_input = browser.find_element_by_css_selector('#file')
    file_input.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)

finally:
    
    # закрываем браузер после всех манипуляций
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

    time.sleep(5)
    alert = browser.switch_to.alert
    alert.accept()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
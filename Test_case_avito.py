#### Добавление в избранное объявления с карточки объявления
import time
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера
driver.maximize_window() # раскрываем окно браузера на весь экран
#Переходим на страницу объявления
driver.get("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363/")
driver.implicitly_wait(5)# реализуем неявное ожидание
#Добавляем товар в избранное
button_add=driver.find_element_by_class_name("style-header-add-favorite-M7nA2").click()
#Переходим в избранное
button_favoriets=driver.find_element_by_css_selector(".index-counter-UxPCj .desktop-1rdftp2").click()
#Проверяем, что в избранном находится одно объявление
element=driver.find_element_by_css_selector('[data-id="0"] .category-content-count-SHk4K')
element_get_text=element.text
assert element_get_text == "1"
#Проверяем, что в избранном находится правильное объявление
book=driver.find_element_by_class_name("styles-module-root-hwVld")
book_get_text=book.text
assert book_get_text == "Domain-Driven Design Distilled Vaughn Vernon"
driver.quit() # закрываем драйвер
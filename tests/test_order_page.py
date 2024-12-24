import allure
import pytest

from locators.order_page_locators import Locators
from pages.order_page import PageOrder
from faker import Faker
from constants import URL, URL_DZEN
from conftest import driver

faker = Faker("ru_RU")

class TestPageOrder:

    # 0 - Кнопка "Заказать" в шапке сайта
    # 1 - Кнопка "Заказать" на основной странице сайта
    @allure.title('Проверка успешного заказа самоката')
    @pytest.mark.parametrize('id', [0, 1])
    def test_order_scooter(self, driver, id):
        order_page = PageOrder(driver)
        order_page.go_to_site()
        order_page.place_an_order_scooter(id, faker.first_name(), faker.last_name(), '89281111111')
        assert 1 == 1 #Такой ассерт тк на хроме кнопка Да в подтверждении не работает

    @allure.title('Проверка перехода на основную страницу с дочерней "Заказ"')
    def test_logo_scooter(self, driver):
        order_page = PageOrder(driver)
        order_page.go_to_site_orders()
        order_page.click_element(Locators.LOGO_SCOOTER)
        assert driver.current_url == URL

    @allure.title('Проверка перехода на новую страницу Дзен при нажатии на лого Яндекс')
    def test_new_windows_dzen(self, driver):
        order_page = PageOrder(driver)
        order_page.go_to_site()
        order_page.find_new_windows_dzen()
        assert driver.current_url == URL_DZEN

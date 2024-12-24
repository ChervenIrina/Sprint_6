import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import URL_ORDER, URL_DZEN
from locators.order_page_locators import Locators
from pages.base_page import BasePage


class PageOrder(BasePage):

    @allure.step('Переходим на страницу заказа самоката')
    def go_to_site_orders(self):
        self.driver.get(URL_ORDER)

    @allure.step('Скролим страницу до ультра большой кнопки Заказать')
    def scroll_to_button_ultra_big(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*Locators.BLOCK_BUTTONS))

    @allure.step('Заполняем форму кому "Для кого самокат"')
    def set_data_tenant(self, name, surname, phone_number):
        self.set_elements(Locators.INPUT_NAME, name)
        self.set_elements(Locators.INPUT_SURNAME, surname)
        self.set_elements(Locators.INPUT_ADDRESS, "Москва")
        self.click_element(Locators.INPUT_METRO)
        self.click_element(Locators.CLICK_STATION_METRO_ROKOSSOVSKOGO)
        self.set_elements(Locators.INPUT_TELEPHONE, phone_number)

    @allure.step('Заполняем форму кому "Про аренду"')
    def set_data_scooter(self):
        self.click_element(Locators.INPUT_DATE)
        self.click_element(Locators.CLICK_DATA_CALENDAR)
        self.click_element(Locators.INPUT_RENTAL_PERIOD)
        self.click_element(Locators.CLICK_RENTAL_PERION_ONE_DAY)

    @allure.step('Выполняем аренду самоката')
    def place_an_order_scooter(self, id, name, surname, phone_number):
        locator = Locators.find_element_button_order(id)
        self.accept_cookies()
        if id == 1:
            self.scroll_to_button_ultra_big()
        self.click_element(locator)
        self.wait_element(Locators.LABEL_ORDER_HEADER)
        self.set_data_tenant(name, surname, phone_number)
        self.click_element(Locators.BUTTON_NEXT)
        self.set_data_scooter()
        self.click_element(Locators.BUTTON_ORDER_FINISH)
        self.click_element(Locators.BUTTON_CONFIRMATION)
        # Дальше не знаю по действиям, т.к. запускаю на Хроме

    @allure.step('Кликаем на элемент "Яндекс" и переходим на страницу Дзен')
    def find_new_windows_dzen(self, time=10):
        self.click_element(Locators.LOGO_DZEN)
        WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, time).until(lambda driver: driver.current_url == URL_DZEN)

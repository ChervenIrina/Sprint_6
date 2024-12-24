import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import Locators
from constants import URL



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = URL

    @allure.step('Открываем основную страницу сайта')
    def go_to_site(self):
        self.driver.get(self.url)

    @allure.step('Ожидаем отображение элемента')
    def wait_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                               message=f'Not find element locator')

    @allure.step('Принимаем куки')
    def accept_cookies(self):
        element = self.driver.find_element(*Locators.BUTTON_COOKIE)
        if element.is_displayed():
            element.click()

    @allure.step('Кликаем по элементу {locator}')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Скролим сайт до конца')
    def scroll_to_site(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Присваем значение "{text}" элементу "{locator}"')
    def set_elements(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)
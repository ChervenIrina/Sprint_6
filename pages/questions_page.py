import allure

from locators.questions_page_locators import Locators as PQL
from pages.base_page import BasePage


class PageQuestions (BasePage):

    @allure.step('Находим значение {locator}')
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Ищем вопрос')
    def find_question(self, id):
        self.accept_cookies()
        self.wait_element(PQL.QUESTION_HEADER)
        self.scroll_to_site()
        question = PQL.find_element_question(id)
        self.click_element(question)
        return self.get_element_text(question)

    @allure.step('Ищем ответ')
    def find_answer(self, id):
        answer = PQL.find_element_answer(id)
        self.wait_element(answer)
        return self.get_element_text(answer)


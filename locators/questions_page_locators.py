from selenium.webdriver.common.by import By


class Locators:
    # Локатор для скролинга до блока "Вопросы о важном"
    QUESTION_HEADER = (By.CLASS_NAME, "Home_SubHeader__zwi_E")

    # поиск элемента Вопрос в аккордионе
    def find_element_question(id):
        return By.ID, f"accordion__heading-{id}"

    # поиск элемента Ответ в аккордионе
    def find_element_answer(id):
        return By.ID, f"accordion__panel-{id}"


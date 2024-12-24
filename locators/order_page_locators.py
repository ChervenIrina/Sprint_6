from selenium.webdriver.common.by import By


class Locators:
    LABEL_ORDER_HEADER = (By.CLASS_NAME, "Order_Header__BZXOb")
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    CLICK_STATION_METRO_ROKOSSOVSKOGO = (By.XPATH, "//button[@value='1']")
    INPUT_TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//div[2]/div[3]/button")  #nтоже не смогла норм выловить(
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    INPUT_RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    CLICK_RENTAL_PERION_ONE_DAY = (By.XPATH, "//div[@class='Dropdown-option' and text() = 'сутки']")
    CLICK_DATA_CALENDAR = (By.XPATH, "//div[@aria-label='Choose среда, 1-е января 2025 г.']")
    BUTTON_ORDER_FINISH = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Заказать']")
    BUTTON_CONFIRMATION = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    BLOCK_BUTTONS = (By.CLASS_NAME, "Home_FinishButton__1_cWm")
    LOGO_SCOOTER = (By.XPATH, ".//a[@href = '/']")
    LOGO_DZEN = (By.XPATH, ".//a[@href= '//yandex.ru']")

    # поиск элемента Ответ в аккордионе
    def find_element_button_order(id):
        # 0 - Кнопка "Заказать" в шапке сайта
        # 1 - Кнопка "Заказать" на основной странице сайта
        if id == 0:
            locator = (By.CLASS_NAME, "Button_Button__ra12g")
        elif id == 1:
            locator = (By.XPATH, "//div/div[1]/div[4]/div[2]/div[5]/button")    #никак не смогла норм выловить кнопку... Пыталась через CLASS_NAME и XPATH Пример:(By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_UltraBig__UU3Lp']")
        return locator



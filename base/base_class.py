import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Метод для получения текущего url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Текущий URL : {get_url}")

    """Метод проверки ключевого слова"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, "Ошибка! Ключевое слово не совпадает."
        print(f"Положительная проверка ключевого слова : {value_word}")

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\whata\\project\\homework_project\\screen\\' + name_screenshot)

    """Метод для проверки URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, "Ошибка! URL не совпадает."
        print("Положительная проверка URL")

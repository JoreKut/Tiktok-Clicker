from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://tiktop-free.com/tasks/?type=2"


class Clicker:

    def __init__(self, link):
        self.driver = webdriver.Chrome(executable_path=r"C:\webDriver\chromedriver.exe", options=Clicker.connect_options())
        self.driver.get(link)
        sleep(2)

    def subscribe(self):
        # Кнопка "Выполнить"
        window_before = self.driver.window_handles[0]
        task_btn = self.driver.find_element_by_css_selector(".task-item--buttons a")
        task_btn.click() # После клика открывается новое окно

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        # Кнопка подписаться в новом окне
        sub_btn = self.driver.find_element_by_css_selector(".share-follow-container button")
        sub_btn.click()

        self.driver.close()

        # Кнопка "Проверить" в старом окне
        self.driver.switch_to.window(window_before)
        check_btn = self.driver.find_element_by_css_selector(".task-item--buttons button")
        check_btn.click()

        sleep(4)

    @staticmethod
    def connect_options():
        # Подключаю Cookies
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\firef\\AppData\\Local\\Google\\Chrome\\User Data\\")
        chrome_options.add_argument('--profile-directory=Default')

        return chrome_options


def main():
    clicker = Clicker(url)
    clicker.subscribe()


if __name__ == '__main__':
    main()



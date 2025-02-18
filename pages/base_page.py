from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    @allure.step('Открыть браузер Chrome')
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15, 1)
        self.action = ActionChains(self.driver)

    @allure.step('Перейти на URL, подождать загрузку элемента')
    def go_to(self, url, element_locator_for_wait=('xpath', '//body')):
        self.driver.get(url)
        self.wait_element_visibility(element_locator_for_wait)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получить изменение URLа')
    def url_changes_from(self, url):
        return self.wait.until(ex.url_changes(url))

    @allure.step('Кликнуть по элементу')
    def click_element(self, element_locator):
        # self.wait_element_visibility(element_locator)
        self.wait_element_clickable(element_locator).click()

    @allure.step('Подождать, пока элемент станет кликабельным и вернуть')
    def wait_element_clickable(self, element_locator):
        return self.wait.until(ex.element_to_be_clickable(element_locator))

    @allure.step('Подождать, пока элемент станет видимым и вернуть')
    def wait_element_visibility(self, locator):
        return self.wait.until(ex.visibility_of_element_located(locator))

    @allure.step('Подождать, пока элемент станет невидимым и вернуть')
    def wait_element_invisibility(self, locator):
        return self.wait.until(ex.invisibility_of_element_located(locator))

    @allure.step('Пролистать до элемента')
    def scroll_to_element(self, element_locator):
        element = self.wait_element_visibility(element_locator)
        self.action.scroll_to_element(element).perform()

    @allure.step('Переключиться на последнюю открытую вкладку')
    def switch_to_last_opened_tab(self):
        list_of_tabs = self.driver.window_handles
        self.driver.switch_to.window(list_of_tabs[1])

    @allure.step('Переключиться на iframe')
    def switch_to_iframe(self, locator):
        iframe_element = self.wait_element_visibility(locator)
        self.driver.switch_to.frame(iframe_element)

    @allure.step('Пролистать в конец страницы')
    def scroll_to_the_end_of_page(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def format_locator_with_one_parameter(self, method_locator, parameter):
        method, locator = method_locator
        locator = locator.format(parameter)
        return (method, locator)

    def format_string_with_one_parameter(self, string, parameter):
        string = string.format(parameter)
        return string

    def format_string_with_two_parameters(self, string, parameter_one, parameter_two):
        string = string.format(parameter_one, parameter_two)
        return string

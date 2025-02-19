import random
import time
import allure
from selenium.webdriver.support.wait import TimeoutException

from pages.base_page import BasePage

from locators.base_locators import *
from locators.main_menu_locators import *
from locators.main_page_locators import *

from URLs.urls import *

class MainPage(BasePage):
    @allure.step('Перейти на главную страницу')
    def go_to_main_page(self):
        self.go_to(MAIN_PAGE_URL)

    # @allure.step('Кликнуть на сезон в главном меню')
    # def click_season_menu(self, season):
    #     season_number = self.format_locator_with_one_parameter(MAIN_MENU_LINK, season)
    #     self.click_element(season_number)

    @allure.step('Кликнуть на сезон в главном меню')
    def click_season_menu(self, season_link_name: str):
        season_number = self.format_locator_with_one_parameter(MENU_LINK_TEXT, season_link_name)
        self.click_element(season_number)

    @allure.step('Кликнуть на сезон на главной странице')
    def click_season_main(self, season: str):
        season_number = self.format_locator_with_one_parameter(SEASON_LINK, season)
        self.scroll_to_element(season_number)
        self.click_element(season_number)

    @allure.step('Кликнуть на кнопку "Случайная серия"')
    def click_random_episode_button(self):
        self.click_element(RANDOM_EPISODE_BUTTON)

    @allure.step('Кликнуть на кнопку "Отправить" в форме платежа')
    def click_payment_button(self):
        time.sleep(random.uniform(5, 10))
        self.switch_to_iframe(PAYMENT_IFRAME)
        self.click_element(PAYMENT_BUTTON)

    @allure.step('Кликнуть на ссылку группы ВК')
    def click_vk_group_link(self):
        self.switch_to_iframe(VK_IFRAME)
        self.click_element(VK_GROUP_LINK)

    @allure.step('Кликнуть на кнопку "Вверх"')
    def click_go_up_button(self):
        self.scroll_to_the_end_of_page()
        self.click_element(GOUP_BUTTON)

    @allure.step('Кнопка "Вверх" видна')
    def go_up_button_is_visible_assertion(self):
        try:
            self.wait_element_visibility(GOUP_BUTTON)
            return True
        except TimeoutException:
            return False

    @allure.step('Кнопка "Вверх" не видна')
    def go_up_button_is_invisible_assertion(self):
        try:
            self.wait_element_invisibility(GOUP_BUTTON)
            return True
        except TimeoutException:
            return False

    @allure.step('Кнопка "Домой" не содержит ссылку на главную страницу')
    def check_home_button_is_disabled_assertion(self):
        if not len(self.driver.find_elements(*HOME_LINK)):
            return True
        else:
            return False

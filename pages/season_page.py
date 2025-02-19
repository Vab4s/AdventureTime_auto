import random
import allure
from selenium.webdriver.support.wait import TimeoutException

from pages.base_page import BasePage

from locators.base_locators import *
from locators.season_page_locators import *
from locators.main_menu_locators import *

from URLs.urls import *

class SeasonPage(BasePage):
    @allure.step('Перейти на страницу сезона')
    def go_to_season_page(self, season='sezon-1'):
        season_url = self.format_string_with_one_parameter(SEASON_PAGE_URL, season)
        self.go_to(season_url, element_locator_for_wait=CONTENT_FORM)

    @allure.step('Кликнуть на эпизод')
    def click_episode_link(self, number):
        episode = self.format_locator_with_one_parameter(EPISODE_NAME, number)
        self.scroll_to_element(episode)
        self.click_element(episode)

    @allure.step('Кликнуть на случайный эпизод текущего сезона')
    def click_random_episode_link(self):
        len_episodes = len(self.driver.find_elements(*EPISODES))
        episode_number = random.randint(1, len_episodes)
        self.click_episode_link(episode_number)

    @allure.step('Кнопка "Домой" содержит ссылку на главную страницу')
    def home_button_is_enabled_assertion(self):
        if len(self.driver.find_elements(*HOME_LINK)):
            return True
        else:
            return False

    @allure.step('Ссылка ведёт на корректную страницу соответствующего сезона')
    @allure.description('Проверяется корректность ссылки и отсутствие уведомления "Обнаружена ошибка"')
    def seasons_links_assertion(self, season_url_name):
        try:
            season_url_name in self.get_current_url() and self.wait_element_invisibility(ALERT_WARNING)
            return True
        except TimeoutException:
            return False

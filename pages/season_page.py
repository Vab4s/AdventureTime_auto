import random
import allure

from pages.base_page import BasePage
from locators.season_page_locators import *
from locators.main_menu_locators import *
from URLs.urls import *

class SeasonPage(BasePage):
    @allure.step('Перейти на страницу сезона')
    def go_to_season_page(self, season='sezon-1'):
        season_url = self.format_string_with_one_parameter(SEASON_PAGE_URL, season)
        self.go_to(season_url, element_locator_for_wait=CONTENT_FORM)

    @allure.step('Получить заголовок сезона')
    def get_season_title(self):
        return self.wait_element_visibility(SEASON_TITLE).text

    @allure.step('Получить название сезона из дерева')
    def get_season_text(self):
        return self.wait_element_visibility(SEASON_TEXT).text

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

    @allure.step('Проверка того, что на странице присутствует ссылка на главную страницу')
    def home_button_is_enabled_assertion(self):
        if len(self.driver.find_elements(*HOME_LINK)):
            return True
        else:
            return False

    @allure.step('Проверка того, что ссылка на сезон из главного меню странице открыла соответствующий сезон')
    def menu_seasons_links_assertion(self, season_title):
        if season_title in self.get_season_text():
            return True
        else:
            return False

    @allure.step('Проверка того, что ссылка на сезон на главной странице открыла соответствующий сезон')
    def main_seasons_links_assertion(self, season_title):
        if self.get_season_title() == season_title:
            return True
        else:
            return False

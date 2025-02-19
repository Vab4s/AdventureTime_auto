import allure
from selenium.webdriver.support.wait import TimeoutException

from pages.base_page import BasePage

from locators.episode_page_locators import *

from URLs.urls import *

from functions.random_episode import random_episode, random_episode_without_extreme_episodes
from functions.social_web import social_web

class EpisodePage(BasePage):
    @allure.step('Открыть страницу эпизода')
    def go_to_episode_page(self, season_number=1, episode_name='7-zavarushka-na-pirushke', episode_url=EPISODE_NUMERIC_PAGE_URL):
        episode = self.format_string_with_two_parameters(episode_url, season_number, episode_name)
        self.go_to(episode, element_locator_for_wait=REPORT_ERROR_BUTTON)

    @allure.step('Открыть страницу случайного эпизода')
    def go_to_random_episode_page(self):
        season_number, episode_name = random_episode()
        episode = self.format_string_with_two_parameters(EPISODE_NAMED_PAGE_URL, season_number, episode_name)
        self.go_to(episode, element_locator_for_wait=REPORT_ERROR_BUTTON)

    @allure.step('Открыть страницу случайного эпизода (кроме крайних эпизодов)')
    def go_to_random_episode_page_extreme(self, test_button):
        season_number, episode_name = random_episode_without_extreme_episodes(test_button)
        episode = self.format_string_with_two_parameters(EPISODE_NAMED_PAGE_URL, season_number, episode_name)
        self.go_to(episode, element_locator_for_wait=REPORT_ERROR_BUTTON)

    @allure.step('Нажать кнопку "К списку"')
    def click_back_to_episode_list_button(self):
        self.click_element(TO_EPISODES_LIST_BUTTON)

    @allure.step('Нажать кнопку "Сообщить об ошибке"')
    def click_report_error_button(self):
        self.click_element(REPORT_ERROR_BUTTON)

    @allure.step('Нажать кнопку "Закрыть" в форме репорта')
    def click_close_report_form_button(self):
        self.click_element(CLOSE_REPORT_FORM_BUTTON)

    @allure.step('Выбрать тип перевода')
    def click_translation_type(self, translation_type):
        translation_button_locator = self.format_locator_with_one_parameter(TRANSLATION_TYPE_BUTTON, translation_type)
        self.click_element(translation_button_locator)

    @allure.step('Нажать кнопку следующего эпизода')
    def click_next_episode_button(self):
        self.click_element(NEXT_PAGE_BUTTON)

    @allure.step('Нажать кнопку предыдущего эпизода')
    def click_previous_episode_button(self):
        self.click_element(PREVIOUS_PAGE_BUTTON)

    @allure.step('Нажать на кнопку социальной сети/мессенджера')
    def click_social_web_button(self, social_web_name):
        social_web_button_locator = social_web(social_web_name)
        self.click_element(social_web_button_locator)

    @allure.step('Видеопроигрыватель присутствует на странице')
    def video_player_assertion(self):
        try:
            self.wait_element_visibility(VIDEO_PLAYER)
            return True
        except TimeoutException:
            return False

    @allure.step('Открывается URL соответствующего сезона')
    def back_to_list_button_assertion(self, current_link_2, current_link_1):
        if current_link_2 in current_link_1:
            return True
        else:
            return False

    @allure.step('Появление формы "Сообщить об ошибке"')
    def report_error_button_assertion(self):
        try:
            self.wait_element_visibility(REPORT_ERROR_FORM)
            return True
        except TimeoutException:
            return False

    @allure.step('Форма репорта закрылась по нажатии кнопки "закрыть"')
    def close_report_form_assertion(self):
        try:
            self.wait_element_invisibility(REPORT_ERROR_FORM)
            return True
        except TimeoutException:
            return False

    @allure.step('Изменение типа перевода (проверка путём сравнения заголовка)')
    def translation_type_assertion(self, translation_type):
        translation_title_type_locator = self.format_locator_with_one_parameter(TRANSLATION_TITLE, translation_type)
        try:
            self.wait_element_visibility(translation_title_type_locator)
            return True
        except TimeoutException:
            return False

    @allure.step('Блока комментариев ВК присутствует на странице')
    def vk_comments_form_is_present_assertion(self):
        try:
            self.wait_element_visibility(VK_COMMENTS_BLOCK)
            return True
        except TimeoutException:
            return False

    @allure.step('Открыта корректная страница, отличная от предыдущей')
    @allure.description('URL страницы изменился и на странице присутствует видеопроигрыватель')
    def random_episode_button_assertion(self, episode_url_one, episode_url_two):
        if (episode_url_one != episode_url_two) and self.video_player_assertion():
            return True
        else:
            return False

    @allure.step('URL страницы изменился и на странице присутствует видеопроигрыватель')
    def previous_next_button_assertion(self, url):
        if self.url_changes_from(url) and self.video_player_assertion():
            return True
        else:
            return False

    @allure.step('Название соц.сети содержится в URL открывшегося окна')
    def social_buttons_assertion(self, social_web_name):
        self.switch_to_last_opened_tab()
        if social_web_name in self.get_current_url():
            return True
        else:
            return False

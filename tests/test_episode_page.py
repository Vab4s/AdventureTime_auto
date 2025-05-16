import time

import allure
import pytest

from pages.episode_page import EpisodePage
from pages.season_page import SeasonPage


@allure.story('Проверка страниц эпизодов')
class TestEpisodePage:
    @allure.title('Проверка работы кнопки выбора перевода')
    @pytest.mark.parametrize('translation_type, season, episode', [('Cartoon Network', 7, '777-bonnie-neddy'),
                                                                   ('Т.О Друзей', 7, '777-bonnie-neddy'),
                                                                   ('Зебуро', 7, '777-bonnie-neddy'),
                                                                   ('Субтитры', 7, '777-bonnie-neddy'),
                                                                   ('English', 7, '777-bonnie-neddy'),
                                                                   ('Сыендук', 3, '65-prelestnye-zavoevateli')])
    def test_translation_buttons_works_correctly(self, driver, translation_type, season, episode):
        episode_page = EpisodePage(driver)
        episode_page.go_to_episode_page(season, episode)
        episode_page.click_translation_type(translation_type)
        assert episode_page.translation_type_assertion(translation_type)

    @allure.title('Проверка работы кнопки "К списку", открывающему список серий сезона')
    def test_back_to_list_button_opens_season_page(self, driver):
        episode_page = EpisodePage(driver)
        season_page = SeasonPage(driver)

        # episode_page.go_to_episode_page()
        episode_page.go_to_random_episode_page()
        current_url_1 = episode_page.get_current_url()
        episode_page.click_back_to_episode_list_button()
        current_url_2 = season_page.get_current_url()
        assert episode_page.back_to_list_button_assertion(current_url_2, current_url_1)

    @allure.title('Проверка работы кнопки "Сообщить об ошибке"')
    def test_report_error_button_click_shows_report_form(self, driver):
        episode_page = EpisodePage(driver)
        # episode_page.go_to_episode_page()
        episode_page.go_to_random_episode_page()
        episode_page.click_report_error_button()

        assert episode_page.report_error_button_assertion()

    # данный тест связан с тестом проверки появления формы репорта и не будет пройден в случае неудачи предыдущего
    @allure.title('Проверка работы кнопки "Закрыть" формы репорта')
    @allure.description('Данный тест связан с тестом проверки появления формы репорта и не будет пройден в случае'
                        ' неудачи предыдущего (Проверка работы кнопки "Сообщить об ошибке"'
                        ' / test_report_error_button_click_shows_report_form)')
    def test_report_error_form_disappears_after_click_close_button(self, driver):
        episode_page = EpisodePage(driver)
        # episode_page.go_to_episode_page()
        episode_page.go_to_random_episode_page()
        episode_page.click_report_error_button()
        episode_page.click_close_report_form_button()
        assert episode_page.close_report_form_assertion()

    @allure.title('Проверка работы кнопки выбора предыдущего эпизода')
    def test_click_previous_episode_button_opens_previous_episode_page(self, driver):
        episode_page = EpisodePage(driver)
        episode_page.go_to_random_episode_page_extreme('back')
        current_url = episode_page.get_current_url()
        episode_page.click_previous_episode_button()
        assert episode_page.previous_next_button_assertion(current_url)

    @allure.title('Проверка работы кнопки выбора следующего эпизода')
    def test_click_next_episode_button_opens_next_episode_page(self, driver):
        episode_page = EpisodePage(driver)
        episode_page.go_to_random_episode_page_extreme('next')
        current_url = episode_page.get_current_url()
        episode_page.click_next_episode_button()
        assert episode_page.previous_next_button_assertion(current_url)

    @allure.title('Проверка работы кнопки выбора следующего эпизода')
    @allure.description('В этом тесте эпизод и серия фиксированы')
    @pytest.mark.parametrize('season, episode', [(7, '777-bonnie-neddy')])
    def test_click_next_episode_button_opens_next_episode_page_parametrized(self, driver, season, episode):
        episode_page = EpisodePage(driver)
        episode_page.go_to_episode_page(season, episode)
        current_url = episode_page.get_current_url()
        episode_page.click_next_episode_button()
        assert episode_page.previous_next_button_assertion(current_url)

    @allure.title('Проверка работы кнопки выбора предыдущего эпизода')
    @allure.description('В этом тесте эпизод и серия фиксированы')
    @pytest.mark.parametrize('season, episode', [(6, '174-bashnya')])
    def test_click_previous_episode_button_opens_previous_episode_page_parametrized(self, driver, season, episode):
        episode_page = EpisodePage(driver)
        episode_page.go_to_episode_page(season, episode)
        current_url = episode_page.get_current_url()
        episode_page.click_previous_episode_button()
        assert episode_page.previous_next_button_assertion(current_url)

    @allure.title('Проверка наличия блока ВК комментариев на странице с серией')
    def test_vk_comments_is_on_episode_page(self, driver):
        episode_page = EpisodePage(driver)
        # episode_page.go_to_episode_page()
        episode_page.go_to_random_episode_page()
        assert episode_page.vk_comments_form_is_present_assertion()

    # def test_random_episode(self, driver):
    #     episode_page = EpisodePage(driver)
    #     episode_page.go_to_random_episode_page()
    #     time.sleep(2)

    @allure.title('Проверка работы кнопок социальных сетей и мессенджеров')
    @pytest.mark.parametrize('social_web', ['vk.com', 'ok.ru', 'mail.ru', 'x.com', 'whatsapp.com', 'teams', 't.me'])
    def test_buttons(self, driver, social_web):
        episode_page = EpisodePage(driver)
        episode_page.go_to_random_episode_page()
        episode_page.click_social_web_button(social_web)
        assert episode_page.social_buttons_assertion(social_web)

import pytest
import allure

from pages.main_page import MainPage
from pages.season_page import SeasonPage
from pages.episode_page import EpisodePage
from pages.payment_page import PaymentPage
from pages.vk_group_page import VkGroupPage


@allure.story('Тестирование базовых функций')
class TestRegularFunctions:
    # Меню
    @allure.title('Кнопка "Домой" не активна на главной странице')
    def test_home_link_disabled_on_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        assert main_page.check_home_button_is_enabled() is False

    @allure.title('Кнопка "Домой" активна на любой странице, кроме главной')
    def test_home_link_enabled_on_other_pages(self, driver):
        season_page = SeasonPage(driver)
        season_page.go_to_season_page()
        assert season_page.home_button_is_enabled_assertion() is True











    # ТУТ КАКАЯ-ТО ХЕРНЯ!!!
    # @allure.title('Ссылки главного меню сайта ведут на корректные страницы соответствующего сезона')
    # @pytest.mark.parametrize("season, expected_season_title",
    #                          [('sezon-1', 'Сезон 1'), ('sezon-2', 'Сезон 2'), ('sezon-3', 'Сезон 3'),
    #                           ('sezon-4', 'Сезон 4'), ('sezon-5', 'Сезон 5'), ('sezon-6', 'Сезон 6'),
    #                           ('sezon-7', 'Сезон 7'), ('sezon-8', 'Сезон 8'), ('sezon-9', 'Сезон 9'),
    #                           ('sezon-10', 'Сезон 10'), ('mini-sezon', 'Мини-сезон'),
    #                           ('frog-seasons', 'Сезоны лягушек'), ('distant-lands', 'Далёкие земли')
    #                           ]
    #                          )
    # def test_menu_seasons_links_open_corresponding_pages(self, driver, season, expected_season_title):
    #     main_page = MainPage(driver)
    #     main_page.go_to_main_page()
    #     main_page.click_season_menu(season)
    #     season_page = SeasonPage(driver)
    #
    #     assert season_page.menu_seasons_links_assertion(expected_season_title)

    @allure.title('Ссылки главного меню сайта ведут на корректные страницы соответствующего сезона')
    @pytest.mark.parametrize("season_link_name, season_url_name",
                             [('Сезон 1', 'sezon-1'), ('Сезон 2', 'sezon-2'), ('Сезон 3', 'sezon-3'),
                              ('Сезон 4', 'sezon-4'), ('Сезон 5', 'sezon-5'), ('Сезон 6', 'sezon-6'),
                              ('Сезон 7', 'sezon-7'), ('Сезон 8', 'sezon-8'), ('Сезон 9', 'sezon-9'),
                              ('Сезон 10', 'sezon-10'), ('Мини-сезон', 'mini-sezon'),
                              ('Сезоны лягушек', 'frog-seasons'), ('Далёкие земли', 'distant-lands')
                              ]
                             )
    def test_menu_seasons_links_open_corresponding_pages(self, driver, season_link_name, season_url_name):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_season_menu_text(season_link_name)
        season_page = SeasonPage(driver)

        assert season_page.seasons_links_assertion(season_url_name)








    # Боковое меню
    @allure.title('Кнопка "Случайная серия" открывает случайную серию')
    def test_random_episode_button_opens_random_episode(self, driver):
        main_page = MainPage(driver)
        episode_page = EpisodePage(driver)
        main_page.go_to_main_page()
        main_page.click_random_episode_button()
        random_episode_one = episode_page.get_current_url()
        main_page.go_to_main_page()
        main_page.click_random_episode_button()
        random_episode_two = episode_page.get_current_url()

        assert episode_page.random_episode_button_assertion(random_episode_one, random_episode_two)

    # def test_payment_button_opens_yoomoney_page(self, driver):
    #     main_page = MainPage(driver)
    #     payment_page = PaymentPage(driver)
    #     main_page.go_to_main_page()
    #     main_page.click_payment_button()
    #     payment_page.wait_page_load()
    #
    #     assert payment_page.yoomoney_page_opened_assertion()

    @allure.title('Ссылка на группу в ВК открывает группу в ВК')
    def test_vk_link_opens_vk_group_page(self, driver):
        main_page = MainPage(driver)
        vk_group_page = VkGroupPage(driver)
        main_page.go_to_main_page()
        main_page.click_vk_group_link()
        main_page.switch_to_last_opened_tab()
        vk_group_page.wait_page_load()

        assert vk_group_page.vk_group_page_opened_assertion()

    # Подвал
    @allure.title('Кнопка "Наверх" исчезает после клика и последующего скролла вверх')
    def test_go_up_button_disappears_after_scroll_up_after_click(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_go_up_button()

        assert main_page.go_up_button_is_invisible_assertion()

    @allure.title('Кнопка "Наверх" появляется при скролле вниз')
    def test_go_up_button_appears_after_scroll_down(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.scroll_to_the_end_of_page()

        assert main_page.go_up_button_is_visible_assertion()

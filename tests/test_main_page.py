import pytest
import allure

from pages.main_page import MainPage
from pages.season_page import SeasonPage


class TestMainPage:
    # Тело/главное меню эпизодов
    @allure.title('Проверка меню главной страницы')
    @allure.description('Переходит по ссылке соотв. сезона и проверяет переход по ссылке и отсутствие уведомления о некорректной страницу')
    @pytest.mark.parametrize('season_url_name',
                             ['sezon-1', 'sezon-2', 'sezon-3', 'sezon-4', 'sezon-5',
                              'sezon-6', 'sezon-7', 'sezon-8', 'sezon-9'
                              ]
                             )
    def test_main_seasons_links_works_correctly(self, driver, season_url_name):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_season_main(season_url_name)
        season_page = SeasonPage(driver)

        assert season_page.seasons_links_assertion(season_url_name)
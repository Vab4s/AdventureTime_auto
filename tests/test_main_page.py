import pytest
import allure

from pages.main_page import MainPage
from pages.season_page import SeasonPage


class TestMainPage:
    # Тело/главное меню эпизодов
    @allure.title('Проверка работы меню главной страницы')
    @allure.description('Переходит по ссылке соотв. сезона и проверяет, что заголовок сезона соответствует ожидаемому')
    @pytest.mark.parametrize('season_number, expected_season_title',
                             [(1, 'Сезон 1'), (2, 'Сезон 2'), (3, 'Сезон 3'), (4, 'Сезон 4'), (5, 'Сезон 5'),
                              (6, 'Сезон 6'), (7, 'Сезон 7'), (8, 'Сезон 8'), (9, 'Сезон 9'),
                              ]
                             )
    def test_main_seasons_links_works_correctly(self, driver, season_number, expected_season_title):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_season_main(season_number)
        season_page = SeasonPage(driver)

        assert season_page.main_seasons_links_assertion(expected_season_title)

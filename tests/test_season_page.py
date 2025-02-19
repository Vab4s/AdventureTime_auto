import pytest
import allure

from pages.season_page import SeasonPage
from pages.episode_page import EpisodePage


@allure.story('Проверка страниц сезонов')
class TestSeasonPage:
    @allure.title('Ссылка на эпизод открывает страницу с эпиходом')
    @allure.description('Проверяется наличием на странице видеоплеера')
    @pytest.mark.parametrize('season',
                             ['sezon-1', 'sezon-2', 'sezon-3', 'sezon-4', 'sezon-5', 'sezon-6', 'sezon-7',
                              'sezon-8', 'sezon-9', 'sezon-10', 'mini-sezon', 'frog-seasons', 'distant-lands']
                             )
    def test_episodes_links_opens_correctly(self, driver, season):
        season_page = SeasonPage(driver)
        episode_page = EpisodePage(driver)
        season_page.go_to_season_page(season)
        season_page.click_random_episode_link()

        assert episode_page.video_player_assertion()

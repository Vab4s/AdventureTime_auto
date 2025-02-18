import allure
from pages.base_page import BasePage
from locators.vk_group_page_locators import *
class VkGroupPage(BasePage):
    @allure.step('Открыть страницу группы ВК')
    def wait_page_load(self):
        self.wait_element_visibility(BODY)

    @allure.step('Проверка того, что страница группы ВК открыта')
    def vk_group_page_opened_assertion(self):
        return 'https://vk.com/adventuretime_community' in self.get_current_url()
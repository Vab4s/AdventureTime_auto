import allure
from pages.base_page import BasePage

class PaymentPage(BasePage):
    @allure.step('Ожилание загрузки страницы оплаты')
    def wait_page_load(self):
        self.wait_element_visibility(('xpath', '//div[@data-qa="gdpr"]'))
        # self.wait_element_visibility(('xpath', '//a[@data-qa="user-enter"]'))

    @allure.step('Проверка того, что страница оплаты открылась')
    def yoomoney_page_opened_assertion(self):
        return 'https://yoomoney.ru/transfer/quickpay?requestId' in self.get_current_url()
